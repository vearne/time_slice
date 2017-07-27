# encoding=utf-8
class TimeSlice


class TimeFrameUtils(object):
    @staticmethod
    def merge(record_list):
        record_list = sorted(record_list, key=lambda x: x['start_time'])
        return TimeFrame.aggs(record_list)

    @staticmethod
    def minus(record_list1, record_list2):
        if len(record_list2) <= 0:
            return record_list1

        record_list1 = TimeFrame.merge(record_list1)
        record_list2 = TimeFrame.merge(record_list2)

        res_list = []
        for record2 in record_list2:
            res_list = []
            for record1 in record_list1:
                res_list.extend(TimeFrame.minus_record(record1, record2))
                record_list1 = res_list

        res_list = TimeFrame.merge(res_list)
        return res_list

    @staticmethod
    def minus_record(record1, record2):
        if not TimeFrame.is_overlap(record1, record2):
            return [record1]

        res = []
        if record1['start_time'] <= record2['start_time'] and record1['end_time'] >= record2['end_time']:
            temp = {
                "start_time": record1['start_time'],
                "end_time": record2['start_time']
            }
            res.append(temp)
            temp = {
                "start_time": record2['end_time'],
                "end_time": record1['end_time']
            }
            res.append(temp)
        elif record1['start_time'] <= record2['start_time'] and record1['end_time'] <= record2['end_time']:
            temp = {
                "start_time": record1['start_time'],
                "end_time": record2['start_time']
            }
            res.append(temp)
        elif record1['start_time'] >= record2['start_time'] and record1['end_time'] >= record2['end_time']:
            temp = {
                "start_time": record2['end_time'],
                "end_time": record1['end_time']
            }
            res.append(temp)
        # record1['start_time'] >= record2['start_time'] and record1['end_time'] <= record2['end_time']:
        ll = []
        for record in res:
            if record['end_time'] > record['start_time']:
                ll.append(record)
        return ll

    @staticmethod
    def is_overlap(item1, item2):
        '''
            item1的start_time小于等于item2的start_time
        :param item1:
        :param item2:
        :return:
        '''
        # case 1
        #     |_________|
        #   |_______|
        if item2['end_time'] >= item1['start_time'] and item2['end_time'] <= item1['end_time']:
            return True

        # case 2
        #     |_________|
        #           |_______|
        if item2['start_time'] >= item1['start_time'] and item2['start_time'] <= item1['end_time']:
            return True

        return False

    @staticmethod
    def aggs(record_list):
        if len(record_list) < 2:
            return record_list

        item1 = record_list[0]
        item2 = record_list[1]
        if TimeFrame.is_overlap(item1, item2):
            dd = {
                "start_time": min(item1['start_time'], item2['start_time']),
                "end_time": max(item1['end_time'], item2['end_time'])
            }
            if len(record_list) > 2:
                return TimeFrame.aggs([dd] + record_list[2:])
            else:
                return [dd]
        else:
            return [item1] + TimeFrame.aggs(record_list[1:])
