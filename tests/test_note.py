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

def test_get(mocker):
    mock_cursor = mocker.MagicMock()
    mock_cursor.execute.return_value = None
    mock_cursor.fetchone.return_value = ("1", "Test Note 1", "This is a test note.", 1)

    note = Note.get(mock_cursor, "1")

    assert note is not None
    assert note.id == "1"
    assert note.title == "Test Note 1"
    assert note.content == "This is a test note."
    assert note.is_important is True

def test_get_not_found(mocker):
    mock_cursor = mocker.MagicMock()
    mock_cursor.execute.return_value = None
    mock_cursor.fetchone.return_value = None

    note = Note.get(mock_cursor, "nonexistent_id")

    assert note is None

def test_save(mocker):
    mock_cursor = mocker.MagicMock()
    mock_cursor.execute.return_value = None
    mock_cursor.connection.commit.return_value = None

    note = Note("1", "Test Note", "This is a test note.", True)
    saved_note = note.save(mock_cursor)

    assert saved_note is note

    mock_cursor.connection.commit.assert_called_once()

def test_update(mocker):
    mock_cursor = mocker.MagicMock()
    mock_cursor.execute.return_value = None
    mock_cursor.connection.commit.return_value = None

    note = Note("1", "Old Title", "Old content.", False)
    note.update(mock_cursor, "New Title", "New content.", True)

    assert note.title == "New Title"
    assert note.content == "New content."
    assert note.is_important is True

    mock_cursor.connection.commit.assert_called_once()

def test_delete(mocker):
    mock_cursor = mocker.MagicMock()
    mock_cursor.execute.return_value = None
    mock_cursor.connection.commit.return_value = None

    note = Note("1", "Test Note", "This is a test note.", True)

    note.delete(mock_cursor)

    mock_cursor.execute.assert_called_once_with(
        "DELETE FROM notes WHERE id = ?",
        ("1",)
    )
    mock_cursor.connection.commit.assert_called_once()