from app.script import sample1


def test_sample1_mock_sample2_200(mocker):
    """
    sample2関数が200を返す
    """
    status_code = 200
    url = 'https://hogehoge.com'
    mocker.patch('app.script.sample2', return_value=status_code)
    assert sample1(url) == status_code


def test_sample1_mock_sample2_404(mocker):
    """
    sample2関数が404を返す
    """
    status_code = 404
    url = 'https://fugafuga.com'
    mocker.patch('app.script.sample2', return_value=status_code)
    assert sample1(url) == status_code


def test_sample1_mock_sample2(mocker):
    """
    sample2関数の返値を動的にする
    """
    def return_status_code(url):
        if url == 'https://hogehoge.com':
            return 200
        elif url == 'https://fugafuga.com':
            return 404
        else:
            return 0
    
    mocker.patch('src.script.sample2', side_effect=return_status_code)
    assert sample1('https://hogehoge.com') == 200
    assert sample1('https://fugafuga.com') == 404
    assert sample1('https://pikopiko.com') == 0