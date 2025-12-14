import flet as ft
from icon_container import create_icon_container

is_dark_mode = True
icons_grid = None
favorites = []
favorites_grid = None
search_value = ""  # Armazena o valor da busca


def main(page: ft.Page):
    global search_value

    def toggle_dark_mode(event):
        global is_dark_mode
        is_dark_mode = not is_dark_mode
        page.theme_mode = ft.ThemeMode.DARK if is_dark_mode else ft.ThemeMode.LIGHT
        page.update()

    def favorite_icon(icon_name: str):
        if icon_name in favorites:
            favorites.remove(icon_name)
        else:
            favorites.append(icon_name)

    def show_favorites(event=None):
        page.clean()
        favorites_grid.controls = []

        for icon_name in favorites:
            favorites_grid.controls.append(create_icon_container(
                icon_name=icon_name,
                on_favorite=favorite_icon
            ))
        layout = ft.Column(
            expand=True,
            controls=[
                ft.Text("Ícones favoritos", 
                style=ft.TextStyle(size=24, weight=ft.FontWeight.BOLD)),
                favorites_grid,
                ft.ElevatedButton("Voltar", on_click=show_search_page)
            ]
        )

        page.add(layout)

    def search_icons(event: ft.ControlEvent):
        global search_value
        global icons_grid
        search_value = event.control.value  # Salva o valor da busca
        value_upper = search_value.upper()
        if icons_grid is not None:
            icons_grid.controls = []
            for icon_name in dir(ft.Icons):
                if value_upper in icon_name:
                    icons_grid.controls.append(create_icon_container(
                        icon_name=icon_name,
                        on_favorite=favorite_icon))
            icons_grid.update()

    def show_search_page(event=None):
        page.clean()
        global icons_grid
        global favorites_grid
        global search_value

        search_bar = ft.TextField(
            prefix_icon=ft.Icons.SEARCH,
            hint_text="Digite algo para buscar...",
            on_submit=search_icons,
            value=search_value  # Preenche o campo de busca com o valor salvo
        )

        icons_grid = ft.GridView(
            expand=True,
            max_extent=200,
            controls=[],
            child_aspect_ratio=1.0
        )

        # Se houver valor de busca, filtra os ícones
        if search_value:
            value_upper = search_value.upper()
            for icon_name in dir(ft.Icons):
                if value_upper in icon_name:
                    icons_grid.controls.append(create_icon_container(
                        icon_name=icon_name,
                        on_favorite=favorite_icon))

        favorites_grid = ft.GridView(
            expand=True,
            max_extent=200,
            controls=[],
            child_aspect_ratio=1.0
        )

        layout = ft.Column(
            expand=True,
            controls=[
                search_bar,
                icons_grid,
                ft.ElevatedButton("Alternar Tema Visual", on_click=toggle_dark_mode),
                ft.ElevatedButton("Ver Favoritos", on_click=show_favorites)
            ]
        )
        page.add(layout)

    page.theme_mode = ft.ThemeMode.DARK
    show_search_page()

ft.app(target=main, view=ft.AppView.FLET_APP)