def u(s, encoding):
    'converted other encoding to unicode encoding'
    if isinstance(s, unicode):
        return s
    else:
        return unicode(s, encoding)