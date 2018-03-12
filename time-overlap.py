"""This package Provides alogirthm to check overlap timings
Along with unittests

"""
import time

test_set = [{
    'is_overlapping': False,
    'time_ranges': [{
        'start': '2016-01-21 10:00:00+00:00',
        'end': '2016-01-21 10:00:00+00:00'
    }]
}, {
    'is_overlapping': False,
    'time_ranges': [{
        'start': '2016-01-25 10:00:25+00:00',
        'end': '2016-01-26 10:00:12+00:00'
    }, {
        'start': '2016-01-21 11:25:00+00:00',
        'end': '2016-01-25 09:59:59+00:00'
    }, {
        'start': '2016-01-27 10:00:00+00:00',
        'end': '2016-01-28 15:16:00+00:00'
    }]
}, {
    'is_overlapping': True,
    'time_ranges': [{
        'start': '2016-01-25 10:00:25+00:00',
        'end': '2016-01-26 10:00:12+00:00'
    }, {
        'start': '2016-01-21 11:25:00+00:00',
        'end': '2016-01-25 16:10:23+00:00'
    }, ]
}, {
    'is_overlapping': True,
    'time_ranges': [{
        'start': '2016-01-21 14:21:00+00:00',
        'end': '2016-01-21 14:22:10+00:00'
    }, {
        'start': '2016-01-21 11:25:00+00:00',
        'end': '2016-01-25 13:10:23+00:00'
    }, {
        'start': '2016-01-21 13:10:24+00:00',
        'end': '2016-01-21 13:14:24+00:00'
    }, {
        'start': '2016-01-21 14:31:12+00:00',
        'end': '2016-01-21 14:31:15+00:00'
    }, {
        'start': '2016-01-21 13:14:27+00:00',
        'end': '2016-01-21 14:20:10+00:00'
    }, {
        'start': '2016-01-21 14:25:30+00:00',
        'end': '2016-01-21 14:25:32+00:00'
    }, {
        'start': '2016-01-21 14:27:12+00:00',
        'end': '2016-01-21 14:29:41+00:00'
    }]
}, {
    'is_overlapping': True,
    'time_ranges': [{
        'start': '2016-01-21 14:21:00+00:00',
        'end': '2016-01-21 14:22:10+00:00'
    }, {
        'start': '2016-01-21 11:25:00+00:00',
        'end': '2016-01-25 13:10:23+00:00'
    }, {
        'start': '2016-01-21 14:25:30+00:00',
        'end': '2016-01-21 14:27:32+00:00'
    }, {
        'start': '2016-01-21 13:10:24+00:00',
        'end': '2016-01-21 13:14:24+00:00'
    }, {
        'start': '2016-01-21 13:14:27+00:00',
        'end': '2016-01-21 15:20:10+00:00'
    }, {
        'start': '2016-01-21 14:31:12+00:00',
        'end': '2016-01-21 14:31:15+00:00'
    }, {
        'start': '2016-01-21 14:27:12+00:00',
        'end': '2016-01-21 14:29:41+00:00'
    }]
}]


def isOverlapping(array):
  """
  Method to check if time ranges in array is overlapping or not
  Args:
    array(list): List containng array ranges

  Returns:
    bool: True if time overlaps False otherwise
  """
  pattern = '%Y-%m-%d %H:%M:%S+00:00'
  for entry in array:
    start = int(time.mktime(time.strptime(entry['start'], pattern)))
    end = int(time.mktime(time.strptime(entry['end'], pattern)))
    entry['start'] = start
    entry['end'] = end
  array.sort(key=lambda ele: ele['start'])

  overlapping =  False
  for index in range(len(array)-1):
    first = array[index]
    second = array[index+1]
    if first['end'] > second['start']:
      overlapping = True
  return overlapping


time_ranges= [{
        'start': '2016-01-25 10:00:25+00:00',
        'end': '2016-01-26 10:00:12+00:00'
    }, {
        'start': '2016-01-21 11:25:00+00:00',
        'end': '2016-01-25 16:10:23+00:00'
    }, ]

def run(test_cases):
    for test_case in test_cases:
      if test_case['is_overlapping'] == isOverlapping(test_case['time_ranges']):
          print 'Passing!'
      else:
          print test_case
          print 'Failing'


run(test_set)
