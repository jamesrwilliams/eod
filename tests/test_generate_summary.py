from lib.summary import generate_summary_list


def test_foo():
    output = "No entries - Did you not track your time today?!"
    result = generate_summary_list([])

    assert result == output


def test_default_ordering():
    test_case = [
        {
            "duration": 1800,
            "description": "third",
        },
        {
            "duration": 10800,
            "description": "first",
        },
        {
            "duration": 1800,
            "description": "second",
        },
        {
            "duration": 1800,
            "description": "second",
        }
    ]

    assert generate_summary_list(test_case) == [
        ("first", 10800),
        ("second", 3600),
        ("third", 1800),
    ]
