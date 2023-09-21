from lib._05_exercise_diary_entry import *

def test_initial_parameters():
    diary_entry = DiaryEntry('Entry1', 'This is a diary entry')
    assert diary_entry.title == 'Entry1'
    assert diary_entry.contents == 'This is a diary entry'

def test_format_of_diary_entry():
    diary_entry = DiaryEntry('Entry1', 'This is a diary entry')
    assert diary_entry.format() == "Entry1: This is a diary entry"

def test_count_words_in_diary_entry():
    diary_entry = DiaryEntry('Entry1', 'This is a diary entry')
    assert diary_entry.count_words() == 5

def test_reading_time_for_given_wpm_for_diary_entry():
    diary_entry = DiaryEntry('Entry1', 'donec massa sapien faucibus et molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit sed ullamcorper morbi tincidunt ornare massa eget egestas purus viverra accumsan in nisl nisi scelerisque eu ultrices vitae auctor eu augue ut lectus arcu bibendum at varius vel pharetra vel turpis nunc eget lorem dolor sed viverra ipsum nunc aliquet bibendum enim facilisis gravida neque convallis a cras semper auctor neque vitae tempus quam pellentesque nec nam aliquam sem et tortor consequat id porta nibh venenatis cras sed felis eget velit aliquet sagittis id consectetur purus ut faucibus pulvinar elementum integer enim neque volutpat ac tincidunt vitae semper quis lectus nulla at volutpat diam ut venenatis tellus in metus vulputate eu scelerisque felis imperdiet proin fermentum leo vel orci porta non pulvinar neque laoreet suspendisse interdum consectetur libero id faucibus nisl tincidunt eget nullam non nisi est sit amet facilisis magna etiam tempor orci eu lobortis elementum nibh tellus molestie nunc non blandit massa enim nec dui nunc mattis enim ut tellus elementum sagittis vitae et leo duis ut diam quam nulla porttitor massa id neque aliquam vestibulum morbi blandit cursus risus at ultrices mi tempus imperdiet nulla malesuada pellentesque elit eget gravida cum sociis natoque')
    assert diary_entry.reading_time(10) == 20

def test_reading_chunk_returns_all_words_for_short_string_at_10wpm_10minutes():
    diary_entry = DiaryEntry('Entry1', "one two three four five six seven eight nine ten")
    reading_chunk = diary_entry.reading_chunk(10, 10)
    assert reading_chunk == "one two three four five six seven eight nine ten"

def test_reading_chunk_returns_first_hundred_words_for_long_string_at_10wpm_10minutes():
    diary_entry = DiaryEntry('Entry1', "one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten")
    reading_chunk = diary_entry.reading_chunk(10, 10)
    assert reading_chunk == 'one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten'

def test_reading_chunk_returns_first_hundred_words_for_long_string_at_10wpm_10minutes():
    diary_entry = DiaryEntry('Entry1', "one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten")
    reading_chunk = diary_entry.reading_chunk(10, 10)
    reading_chunk = diary_entry.reading_chunk(10, 10)
    assert reading_chunk == 'one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten'