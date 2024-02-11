from rich.console import Console
from rich.table import Table
from roman import toRoman
from bs4 import BeautifulSoup

def get_text(html):
    return BeautifulSoup(html, 'html.parser').get_text()

def render(obj, langs):
    console = Console()
    #console.print(obj)

    for lang in obj:
        console.print(f"\n[bold red]{lang['lang'].upper()} > {langs.replace(lang['lang'], '').upper()}[/bold red]")
        for hit in lang['hits']:
            for i, rom in enumerate(hit['roms']):
                console.print(f"\n[bold yellow]{toRoman(i + 1)}. {rom['headword']}[/bold yellow]")
                for arab in rom['arabs']:
                    console.print(f"\n[bold green]{get_text(arab['header'])}[/bold green]")
                    grid = Table.grid(expand=True)
                    grid.add_column(ratio=1)
                    grid.add_column(ratio=1)
                    for translation in arab['translations']:
                        grid.add_row(get_text(translation['source']), get_text(translation['target']))
                    console.print(grid)
    print()
