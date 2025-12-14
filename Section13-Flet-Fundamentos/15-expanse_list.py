import flet as ft

def main(page:ft.Page):
    # Lista de perguntas e respostas
    faq_items = [
        {
            "question": "O que é o Flet?",
            "answer": "FLet é uma biblioteca Python para criação de interfaces gráficas de forma simples e rápida"
        },
        {
            "question": "Como instalar o Flet?",
            "answer": "VOcê pode instalar o Flet usando o pip: 'pip install flet'. "
        },
        {
            "question": "Onde posso encontrar a documentação?",
            "answer": "A documentação está no link: 'https://flet.dev/docs'"
        }
    ]
    
    def handle_change(e: ft.ControlEvent):
        print(f"Panel {e.data} toggled")
        
    def handle_delete(e: ft.ControlEvent):
        panel.controls.remove(e.control.data)
        page.update()
    
    def criar_componentes():
        panel = ft.ExpansionPanelList(
            expand_icon_color=ft.Colors.AMBER,        
            elevation=8,
            divider_color=ft.Colors.AMBER,
            on_change=handle_change,        
            expanded_header_padding=ft.Padding(0, 0, 0, 0)        
        )
        
        for item in faq_items:
            exp = ft.ExpansionPanel(
                header=ft.ListTile(
                    title=ft.Text(item["question"]),
                    bgcolor=ft.Colors.BLUE_100,                
                    text_color=ft.Colors.BLUE_900
                ),
                can_tap_header=True,
                bgcolor=ft.Colors.BLUE_50,            
            )
            
            exp.content = ft.Column(
                [
                    ft.ListTile(
                        title=ft.Text(item["answer"]),
                        bgcolor=ft.Colors.BLUE_800
                    ),
                    ft.Row(
                        [
                            ft.TextButton("Marcar como útil",
                                          on_click=lambda e, item=item: page.add(
                                              ft.Text(f"Você marcou a resposta: {item['answer']} como útil",
                                                      color=ft.Colors.GREEN_600)
                                          )),
                            ft.IconButton(ft.Icons.DELETE,
                                          on_click=handle_delete, data=exp)
                        ],
                        alignment=ft.MainAxisAlignment.END
                    )
                ]
            )
            panel.controls.append(exp)

        page.update()
        
        return panel
    
    def reiniciar_pagina(e):
        page.controls.clear()
        page.add(
            ft.ElevatedButton("Reiniciar pagina", on_click=reiniciar_pagina),
            criar_componentes()
        )
        page.update()
    
    panel = criar_componentes()
    page.add(
        ft.ElevatedButton("Reiniciar pagina", on_click=reiniciar_pagina),
        panel
    )

ft.app(target=main)