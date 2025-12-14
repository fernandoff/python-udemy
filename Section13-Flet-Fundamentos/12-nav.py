import flet as ft

def main(page:ft.Page):
    page.title = "NavigationBar"
    page.navigation_bar = ft.NavigationBar(
        destinations= [
            ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Explore"),
            ft.NavigationBarDestination(icon=ft.Icons.COMMUTE, label="Commute"),
            ft.NavigationBarDestination(icon=ft.Icons.BOOKMARK_BORDER,
                                        label="Explore",
                                        selected_icon=ft.Icons.BOOKMARK
                                        ),
        ]
    )
    page.add(ft.Text("Body"))

ft.app(target=main)