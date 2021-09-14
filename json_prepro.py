
import jmespath

test_dictionary = {
    'level_1': {
        'level_2_a': {
            'level_3_a': 'some_string'
        },
        'level_2_b': {
            'level_3_b': 'a_different_string'
        }
    }
}

# method 1
level_3_a = test_dictionary.get('level_1', {}).get('level_2_a', {}).get('level_3_a', '')

# method 2 : JMESPath
expression = jmespath.compile('level_1.level_2_a.level_3_a')
result = expression.search(test_dictionary)

# https://samuel-vidovich.medium.com/3-cool-python-libraries-that-will-save-you-time-and-effort-27fcdc6762d5
