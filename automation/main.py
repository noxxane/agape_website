def p_surround(paragraph: str):
    return "<p>" + paragraph + "</p>"


def p_surround_with_class_name(paragraph: str, class_name: str):
    return f'<p class="{class_name}">' + paragraph + "</p>"


def masthead_sine_image_to_html(author: str, title: str, section: str, date: str):
    section_header = p_surround_with_class_name(section, "section_header")
    article_header = p_surround_with_class_name(title, "article_header")
    article_author = p_surround_with_class_name(author, "article_author")
    article_date = p_surround_with_class_name(author, "article_date")

    line_list = [section_header, article_header, article_author, article_date]

    return line_list


def article_body_to_html(article_body: str):
    article_body_paragraphs: list[str] = [x.strip() for x in article_body.split("\n")]
    for paragraph in article_body_paragraphs:
        if bool(paragraph) is not True:
            article_body_paragraphs.remove(paragraph)

    article_body_paragraphs = list(map(p_surround, article_body_paragraphs))

    return article_body_paragraphs


if __name__ == "__main__":
    test_body = ""
    with open("lorem_ipsum.txt", "r") as f:
        test_body = f.read()
    article_body = article_body_to_html(test_body)

    section = "Feature"
    title = "Piss Champion of the World"
    author = "Evan Corvino"
    date = "December 7th, 1941"

    masthead = masthead_sine_image_to_html(author, title, section, date)

    print(article_body)
    print(masthead)
