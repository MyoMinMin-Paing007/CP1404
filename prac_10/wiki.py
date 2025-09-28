import wikipedia


def main():
    """Get user input for page title and display the title, summary and url of the page."""
    page_title = input("Input the page title: ")
    while page_title:
        try:
            searched_page = wikipedia.page(page_title)
            print(f"Title: {searched_page.title}")
            print(f"Summary: {searched_page.summary}")
            print(f"URL: {searched_page.url}")
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        except wikipedia.exceptions.PageError:
            print(f"{page_title} does not match any pages. Try another query!")
        page_title = input("Input the page title: ")


main()

