import flet as ft

def main(page:ft.Page):    
    page.title = "Meu App Flet"

    page.add(ft.Text(
        value = "Hello world! asdlahsjd hakjshdg kajshd as dahskdjhakl jshdkja h skldjgh aklsdgaklsg dklhagskldgaksdgkhlasgdlkagsdhjklgaljkdsfg as ajldgs cfjkl afgsdf gaihs dhjkl ajksdfgajshgd fjlaghsfg dkljafs dghjklaf jsd ajlghs dfjl",
        color = "blue",
        theme_style = ft.TextThemeStyle.HEADLINE_LARGE,
        bgcolor = "#FFFFFF",
        style= ft.TextStyle(
            italic = True,
            font_family="Arial"
        ),
        max_lines = 2,
        overflow = ft.TextOverflow.ELLIPSIS,
        text_align= ft.TextAlign.CENTER,
    ))

    page.add(ft.Text(
        value="Hello aaa")
    )
    page.bgcolor = "#3E5250"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.update()

    #Desktop
    # page.window_width = 600
    # page.window_height = 400
    # page.window.full_screen = False

    t1 = ft.Text(
        value="Utilizando Elemento de Texto Utilizando Elemento de TextoUtilizando Elemento de Texto",
        theme_style=ft.TextThemeStyle.DISPLAY_LARGE,
        bgcolor=ft.Colors.WHITE30,
        style=ft.TextStyle(
            color=ft.Colors.BLACK38,
            font_family="Arial",
            italic=True,
            weight=ft.FontWeight.W_300
        ),
        max_lines=2,
        overflow=ft.TextOverflow.ELLIPSIS,
        text_align=ft.TextAlign.CENTER
    )
    text_one_style = ft.TextStyle(color=ft.Colors.CYAN_ACCENT_200,
                                  decoration=ft.TextDecoration.UNDERLINE)

    text_two_style = ft.TextStyle(bgcolor=ft.Colors.INDIGO_900,
                                  color=ft.Colors.RED_400,
                                  decoration=ft.TextDecoration.OVERLINE,
                                  decoration_color=ft.Colors.GREEN,
                                  decoration_style=ft.TextDecorationStyle.DOUBLE)
    t2 = ft.Text(
        spans=[
            ft.TextSpan(text="Texto de exemplo",
                        url="https://www.google.com",
                        style=text_one_style),
            ft.TextSpan(text="Continuação do texto", style=text_two_style)
        ]
    )
    page.add(t1, t2)


    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    page.theme_mode = ft.ThemeMode.LIGHT

    # Adicionando a imagem
    img = ft.Image(
        src="https://www.w3schools.com/w3images/lights.jpg",
        border_radius=ft.border_radius.all(100),
        width=1000,
        height=1000,
        tooltip="Imagem Teste"
    )
    page.clean() # LIMPA A TELA ANTES DE ADICIONAR A IMAGEM
    page.add(img)

    page.update()

ft.app(target=main)

