from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "False" or placeholder == '0':
        passed()
    else:
        failed()


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


