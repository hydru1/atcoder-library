def bit_cnt(n):
    #nは64bit未満
    count = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
    count = (count & 0x3333333333333333) + ((count >> 2) & 0x3333333333333333)
    count = (count & 0x0f0f0f0f0f0f0f0f) + ((count >> 4) & 0x0f0f0f0f0f0f0f0f)
    count = (count & 0x00ff00ff00ff00ff) + ((count >> 8) & 0x00ff00ff00ff00ff)
    count = (count & 0x0000ffff0000ffff) + ((count >> 16) & 0x0000ffff0000ffff)
    return int((count & 0x00000000ffffffff) + ((count >> 32) & 0x00000000ffffffff))
