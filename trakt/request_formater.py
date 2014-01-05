# -*- coding: utf-8  -*-


class RequestFormater(object):
    @classmethod
    def format(cls, format_string):
        pass


class TraktRequestFormater(RequestFormater):
    @classmethod
    def format(cls, format_string):
        replace_list = [[u"å",u"a"],[u"ä",u"a"],[u"ö",u"o"],[u" ",u"."]]

        for replace_item in replace_list:
            format_string = format_string.replace(replace_item[0], replace_item[1]).lower()
        return format_string

class ReleaseRequestFormater(RequestFormater):
    @classmethod
    def format(cls, format_string):
        replace_list = [[u"å",u"a"],[u"ä",u"a"],[u"ö",u"o"],[u" ",u"."]]

        for replace_item in replace_list:
            format_string = format_string.replace(replace_item[0], replace_item[1]).lower()
        return format_string

def main():
    print TraktRequestFormater.format(u"Alla är fotografer")



if __name__ == '__main__':
    main()
