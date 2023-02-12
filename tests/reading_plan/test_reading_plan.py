import pytest
from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
from unittest.mock import patch


@pytest.fixture(scope="module")
def mock_file():
    return [
        {
            "url": "https://blog.betrybe.com/novidades/noticia_0.htm",
            "title": "noticia_0",
            "timestamp": "23/11/2020",
            "writer": "Escritor_0",
            "reading_time": 2,
            "summary": "Sumario da noticia_0",
            "category": "Categoria_0",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-bacana",
            "title": "Notícia bacana",
            "writer": "Eu",
            "summary": "Algo muito bacana aconteceu",
            "reading_time": 4,
            "timestamp": "04/04/2021",
            "category": "Ferramentas",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-legal",
            "title": "Notícia bacana 2",
            "writer": "Você",
            "summary": "Algo muito bacana aconteceu de novo",
            "reading_time": 1,
            "timestamp": "07/04/2022",
            "category": "Novidades",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia_3.htm",
            "title": "noticia_3",
            "timestamp": "23/11/2020",
            "writer": "Escritor_3",
            "reading_time": 1,
            "summary": "Sumario da noticia_3",
            "category": "Ferramentas",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia_4.htm",
            "title": "noticia_4",
            "timestamp": "23/11/2020",
            "writer": "Escritor_4",
            "reading_time": 1,
            "summary": "Sumario da noticia_4",
            "category": "Ferramentas",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia_5.htm",
            "title": "noticia_5",
            "timestamp": "23/11/2020",
            "writer": "Escritor_5",
            "reading_time": 1,
            "summary": "Sumario da noticia_5",
            "category": "Categoria_0",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia_6.htm",
            "title": "noticia_6",
            "timestamp": "23/11/2020",
            "writer": "Escritor_6",
            "reading_time": 1,
            "summary": "Sumario da noticia_6",
            "category": "Novidades",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia_7.htm",
            "title": "noticia_7",
            "timestamp": "23/11/2020",
            "writer": "Escritor_7",
            "reading_time": 7,
            "summary": "Sumario da noticia_1",
            "category": "Categoria_7",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia_8.htm",
            "title": "noticia_8",
            "timestamp": "23/11/2020",
            "writer": "Escritor_7",
            "reading_time": 8,
            "summary": "Sumario da noticia_8",
            "category": "Categoria_7",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia_9.htm",
            "title": "noticia_9",
            "timestamp": "23/11/2020",
            "writer": "Escritor_7",
            "reading_time": 5,
            "summary": "Sumario da noticia_9",
            "category": "Categoria_9",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia_10.htm",
            "title": "noticia_10",
            "timestamp": "23/11/2020",
            "writer": "Escritor_10",
            "reading_time": 11,
            "summary": "Sumario da noticia_10",
            "category": "Categoria_9",
        },
    ]


def test_reading_plan_group_news(mock_file):
    with patch(
        "tech_news.analyzer.reading_plan.find_news", return_value=mock_file
    ):
        test = ReadingPlanService.group_news_for_available_time(10)
        print(test)
        assert ReadingPlanService.group_news_for_available_time(10) == {
            "readable": [
                {
                    "unfilled_time": 1,
                    "chosen_news": [
                        (
                            "noticia_0",
                            2,
                        ),
                        (
                            "Notícia bacana",
                            4,
                        ),
                        (
                            "Notícia bacana 2",
                            1,
                        ),
                        (
                            "noticia_3",
                            1,
                        ),
                        (
                            "noticia_4",
                            1,
                        ),
                    ],
                },
                {
                    "unfilled_time": 1,
                    "chosen_news": [
                        (
                            "noticia_5",
                            1,
                        )
                        (
                            "noticia_6",
                            1,
                        )
                        (
                            "noticia_7",
                            7,
                        )
                    ],
                },
                {
                    "unfilled_time": 2,
                    "chosen_news": [
                        (
                            "noticia_8",
                            8,
                        )
                    ],
                },
                {
                    "unfilled_time": 5,
                    "chosen_news": [
                        (
                            "noticia_9",
                            5,
                        )
                    ],
                },
            ],
            "unreadable": [
                ("noticia_10", 11),
            ],
        }

    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        return ReadingPlanService.group_news_for_available_time(0)
