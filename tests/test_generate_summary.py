from lib.summary import generate_summary_list


def test_empty_results():
    assert generate_summary_list([]) == []

def test_tag_filtering():
    test_cases = [
        {
            "duration": 1,
            "description": 'No tags'
        },
        {
            "duration": 2,
            "description": 'Tags (non-filtered)',
            "tags": [],
        },
        {
            "duration": 3,
            "description": 'Tags valid (non-filtered)',
            "tags": ['foo'],
        },
        {
            "duration": 4,
            "description": 'Tags (filtered)',
            "tags": ['foo', 'personal'],
        },
        {
            "duration": 5,
            "description": 'Tags (filtered filtered)',
            "tags": ['personal'],
        },
    ]

    assert generate_summary_list(test_cases) == [
        ("Tags valid (non-filtered)", 3),
        ("Tags (non-filtered)", 2),
        ("No tags", 1),
    ]


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
