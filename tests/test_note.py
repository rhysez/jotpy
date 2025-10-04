from classes.note import Note

def test_list(mocker):
    mock_cursor = mocker.MagicMock()
    mock_cursor.execute.return_value = None
    mock_cursor.fetchall.return_value = [
        ("1", "Test Note 1", "This is a test note.", 1),
        ("2", "Test Note 2", "This is another test note.", 0)
    ]

    notes = Note.list(mock_cursor)

    assert len(notes) == 2
    assert notes[0].id == "1"
    assert notes[0].title == "Test Note 1"
    assert notes[0].content == "This is a test note."
    assert notes[0].is_important is True

    assert notes[1].id == "2"
    assert notes[1].title == "Test Note 2"
    assert notes[1].content == "This is another test note."
    assert notes[1].is_important is False

