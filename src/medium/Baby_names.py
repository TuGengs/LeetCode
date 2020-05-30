# 婴儿名字 (并查集)

# 输入：names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"], \
#            synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]
# 输出：["John(27)","Chris(36)"]

# 多字符串or 返回第一个，多字符串and 返回最后一个
class Solution:
    def trulyMostPopular(self, names, synonyms):
        """
        :type names: List[str]
        :type synonyms: List[str]
        :rtype: List[str]
        """
        import collections
        p, d, q = {}, {}, collections.defaultdict(int)
        for s in synonyms:
            a, b = s[1: -1].split(',')
            pa, pb = p.setdefault(a, [a]), p.setdefault(b, [b]) # 浅拷贝
            # print(pa, pb)
            if pa is not pb:  # 并查集基操，对数组引用进行合并
                # print(p)
                pa.extend(pb)
                # print(p)
                for c in pb:
                    p[c] = pa
                # print(p)
        for name in p:
            d.setdefault(id(p[name]), min(p[name]))  # 取字典序最小名
        for s in names:
            i = s.find('(')
            name, count = s[: i], int(s[i + 1: -1])
            q[name in p and d[id(p[name])] or name] += count  # 未合并过的name单独计数

        result = []
        for name, count in q.items():
            result.append('{}({})'.format(name, count))
        return result

# ["False(2764)","Obcbxb(124)","Csh(238)","Dnsay(72)","Fvkhz(104)","Dwifi(237)","Chhmx(259)","Hljt(51)","Gnplfi(109)","Chycnm(253)","Bnea(179)","Npilye(25)","Kgabb(236)","Fpaf(219)","Msyr(211)","Aeax(646)"]
# ["Fcclu(70)","Dnsay(72)","Qbmk(45)","Unsb(26)","Gauuk(75)","Gnplfi(109)","Hfp(97)","Obcbxb(124)","Ijveol(46)","Fpaf(219)","Qiy(26)","Mcnef(59)","Dhe(79)","Jfq(26)","Ebov(96)","Ofl(72)","Uvkdpn(71)","Avcp(41)","Chycnm(253)","Koaak(53)","Qyqifg(85)","Oltadg(95)","Mwwvj(70)","Naf(3)","Ibink(32)","Ucqh(51)","Mtz(72)","Ard(82)","Hcvcgc(97)","Knpuq(61)","Yeekgc(11)","Ntfr(70)","Bnea(179)","Weusps(79)","Nuq(61)","Drzsnw(87)","Chhmx(259)","Onnev(77)","Kufa(95)","Avmzs(39)","Okwuq(96)","Hljt(51)","Npilye(25)","Axwtno(57)","Kasgmw(95)","Nsgbth(26)","Nzaz(51)","Msyr(211)","Yjc(94)","Jvqg(47)","Alrksy(69)","Aeax(646)","Acohsf(86)","Csh(238)","Nekuam(17)","Kgabb(236)","Fvkhz(104)","Gbkq(77)","Dwifi(237)"]

if __name__ == '__main__':
    a = Solution()
    l = a.trulyMostPopular(["Fcclu(70)","Ommjh(63)","Dnsay(60)","Qbmk(45)","Unsb(26)","Gauuk(75)","Wzyyim(34)","Bnea(55)","Kri(71)","Qnaakk(76)","Gnplfi(68)","Hfp(97)","Qoi(70)","Ijveol(46)","Iidh(64)","Qiy(26)","Mcnef(59)","Hvueqc(91)","Obcbxb(54)","Dhe(79)","Jfq(26)","Uwjsu(41)","Wfmspz(39)","Ebov(96)","Ofl(72)","Uvkdpn(71)","Avcp(41)","Msyr(9)","Pgfpma(95)","Vbp(89)","Koaak(53)","Qyqifg(85)","Dwayf(97)","Oltadg(95)","Mwwvj(70)","Uxf(74)","Qvjp(6)","Grqrg(81)","Naf(3)","Xjjol(62)","Ibink(32)","Qxabri(41)","Ucqh(51)","Mtz(72)","Aeax(82)","Kxutz(5)","Qweye(15)","Ard(82)","Chycnm(4)","Hcvcgc(97)","Knpuq(61)","Yeekgc(11)","Ntfr(70)","Lucf(62)","Uhsg(23)","Csh(39)","Txixz(87)","Kgabb(80)","Weusps(79)","Nuq(61)","Drzsnw(87)","Xxmsn(98)","Onnev(77)","Owh(64)","Fpaf(46)","Hvia(6)","Kufa(95)","Chhmx(66)","Avmzs(39)","Okwuq(96)","Hrschk(30)","Ffwni(67)","Wpagta(25)","Npilye(14)","Axwtno(57)","Qxkjt(31)","Dwifi(51)","Kasgmw(95)","Vgxj(11)","Nsgbth(26)","Nzaz(51)","Owk(87)","Yjc(94)","Hljt(21)","Jvqg(47)","Alrksy(69)","Tlv(95)","Acohsf(86)","Qejo(60)","Gbclj(20)","Nekuam(17)","Meutux(64)","Tuvzkd(85)","Fvkhz(98)","Rngl(12)","Gbkq(77)","Uzgx(65)","Ghc(15)","Qsc(48)","Siv(47)"], ["(Gnplfi,Qxabri)","(Uzgx,Siv)","(Bnea,Lucf)","(Qnaakk,Msyr)","(Grqrg,Gbclj)","(Uhsg,Qejo)","(Csh,Wpagta)","(Xjjol,Lucf)","(Qoi,Obcbxb)","(Npilye,Vgxj)","(Aeax,Ghc)","(Txixz,Ffwni)","(Qweye,Qsc)","(Kri,Tuvzkd)","(Ommjh,Vbp)","(Pgfpma,Xxmsn)","(Uhsg,Csh)","(Qvjp,Kxutz)","(Qxkjt,Tlv)","(Wfmspz,Owk)","(Dwayf,Chycnm)","(Iidh,Qvjp)","(Dnsay,Rngl)","(Qweye,Tlv)","(Wzyyim,Kxutz)","(Hvueqc,Qejo)","(Tlv,Ghc)","(Hvia,Fvkhz)","(Msyr,Owk)","(Hrschk,Hljt)","(Owh,Gbclj)","(Dwifi,Uzgx)","(Iidh,Fpaf)","(Iidh,Meutux)","(Txixz,Ghc)","(Gbclj,Qsc)","(Kgabb,Tuvzkd)","(Uwjsu,Grqrg)","(Vbp,Dwayf)","(Xxmsn,Chhmx)","(Uxf,Uzgx)"])
    print(l)