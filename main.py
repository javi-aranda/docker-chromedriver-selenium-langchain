from langchain.document_loaders import SeleniumURLLoader

def main():
    urls = [
        "https://example.com",
    ]

    loader = SeleniumURLLoader(urls)

    data = loader.load()

    print(data)

if __name__ == "__main__":
    main()
