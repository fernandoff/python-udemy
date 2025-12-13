import flet as ft

def main(page:ft.Page):
    icons_row = ft.Row(
        controls=[
            ft.Icon(name=ft.Icons.FAVORITE, color=ft.Colors.PINK, size=30),
            ft.Icon(name=ft.Icons.AUDIO_FILE, color=ft.Colors.GREEN_400, size=30),
            ft.Icon(name=ft.Icons.BEACH_ACCESS, color=ft.Colors.BLUE, size=30),
            ft.Icon(name="settings", color="#c1c1c1", size=30),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )
    page.add(
        ft.Column(
            controls=[
                icons_row
            ]
        )
    )

ft.app(target=main)