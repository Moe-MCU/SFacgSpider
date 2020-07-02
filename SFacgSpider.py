# -*- coding: UTF-8 -*-
def save(filename, contents):
    fh = open(filename, 'w', encoding='utf-8')
    fh.write(contents)
    fh.close()
def saveimg(filename, contents):
    fh = open(filename, 'wb')
    fh.write(contents)
    fh.close()
def sfnext(url):
    import re,urllib
    html=urllib.request.urlopen(url).read().decode("utf-8")
    xyz1 =re.search('class="btn normal">下一章</a>', html, flags=0).span()
    xyz1=xyz1[0]
    xyz=html[:xyz1]
    xyz=xyz[-40:]
    xyz2=re.search('=',xyz,flags=0).span()
    xyz2=xyz2[1]
    xyz=xyz[xyz2:]
    xyz=xyz[1:][:-2]
    xyz="http://book.sfacg.com"+xyz
    return xyz
def sflast(url):
    import re,urllib
    html=urllib.request.urlopen(urllib.request.Request(url)).read().decode("utf-8")
    syz1 = re.search('class="btn normal">上一章</a>', html, flags=0	).span()
    syz1=syz1[0]
    syz=html[:syz1]
    syz=syz[-200:]
    syz2=re.search('<a href=',syz,flags=0).span()
    syz2=syz2[1]
    syz=syz[syz2:]
    syz=syz[1:][:-2]
    syz="http://book.sfacg.com"+syz
    return syz
def sf(url):
    import requests
    import os
    cookies = {
        '_uab_collina': '159350166750631907738536',
        '48251uvCookieC': '5',
        '.SFCommunity': 'FAD63E5787F8D1E4F10353AF500DA4E73189E281CCF008E557A853C03971EEA554A3BF164C4A3C3D44B6E715C52F55971AABFF8523AC56349F01D56677EEEC468E363F131FEAFE69D8FDB6D993BAB2CA2AE93FE2E3E2809D0356CAED90037417',
        'session_PC': '60EE012B203FC9DFECEB7BADE652220F',
        'UsePCVersion': '1',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Upgrade-Insecure-Requests': '1',
        'Host': 'book.sfacg.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15',
        'Referer': 'http://book.sfacg.com/Novel/48251/MainIndex/',
        'Accept-Language': 'en-us',
        'Connection': 'keep-alive',
        'Proxy-Connection': 'keep-alive',
    }
    html_file=requests.get(url, headers=headers, cookies=cookies)
    html=html_file.text
    try:
        All_num_1 = re.search('<div class="article" id="article">', html, flags=0).span()
        All_num_1 = All_num_1[1]
        all = html[All_num_1:]
        All_num_2 = re.search('<!-- 按钮 -->', all, flags=0).span()
        All_num_2 = All_num_2[0]
        all = all[:All_num_2]
        
        Inside_num_1 = re.search('<div class="article-hd">', all, flags=0).span()
        Inside_num_1 = Inside_num_1[1]
        Inside = all[Inside_num_1:]
        Inside_num_2 = re.search('</div>', Inside, flags=0).span()
        Inside_num_2 = Inside_num_2[0]
        Inside = Inside[:Inside_num_2]
        
        Title_num_1 = re.search('<h1 class="article-title">', Inside, flags=0).span()
        Title_num_1 = Title_num_1[1]
        Title = Inside[Title_num_1:]
        Title_num_2 = re.search('</h1>', Title, flags=0).span()
        Title_num_2 = Title_num_2[0]
        Title = Title[:Title_num_2]
        title_without_md = Title
        Title = "# " + Title

        Author_num_1 = re.search('作者', Inside, flags=0).span()
        Author_num_1 = Author_num_1[1]
        Author = Inside[Author_num_1:]
        Author_num_2 = re.search('</span>', Author, flags=0).span()
        Author_num_2 = Author_num_2[0]
        Author = Author[:Author_num_2]
        Author = "\n"+"## 作者" + Author
        
        UPDate_time_1 = re.search('更新时间', Inside, flags=0).span()
        UPDate_time_1 = UPDate_time_1[1]
        UPDate_time = Inside[UPDate_time_1:]
        UPDate_time_2 = re.search('</span>', UPDate_time, flags=0).span()
        UPDate_time_2 = UPDate_time_2[0]
        UPDate_time = UPDate_time[:UPDate_time_2]
        UPDate_time = "\n"+"#### 更新时间" + UPDate_time
        
        Count_num_1 = re.search('字数', Inside, flags=0).span()
        Count_num_1 = Count_num_1[1]
        Count_num = Inside[Count_num_1:]
        Count_num_2 = re.search('</span>', Count_num, flags=0).span()
        Count_num_2 = Count_num_2[0]
        Count_num = Count_num[:Count_num_2]
        Count_num = "\n"+"#### 字数" + Count_num
        
        a = re.search('<div class="article-content font16" id="ChapterBody" data-class="font16">', all, flags=0).span()
        b = a[1]
        c = all[b:]
        d = re.search('</div>', c, flags=0).span()
        e = d[0]
        f = c[:e]
        bb = re.sub("</p>", "\n", f, count=0, flags=0)
        bb = bb + " "
        bb = re.sub("<p>", " ", bb, count=0, flags=0)
        bb = bb.replace('\r\n', '')
        bb = re.sub("<br>", "", bb, count=0, flags=0)
        
        try:
            mg = re.search("<img src='", bb,flags=0).span()
            mgg=mg[1]
            mggg=bb[mgg:]
            
            mg2 = re.search("' />", mggg,flags=0).span()
            mg22=mg2[0]
            mgf=mggg[:mg22]
            print("文章内图像:"+mgf)
            imgys="<img src='"+mgf+"' />"
            os.system('wget -P img/ '+mgf)
            bb=bb.replace(imgys, '![img1](img/'+mgf[-40:]+')\n')
        except:
            print("无img")
        try:
            mg = re.search("<img src='", bb,flags=0).span()
            mgg=mg[1]
            mggg=bb[mgg:]
            
            mg2 = re.search("' />", mggg,flags=0).span()
            mg22=mg2[0]
            mgf=mggg[:mg22]
            print("文章内图像:"+mgf)
            imgys="<img src='"+mgf+"' />"
            os.system('wget -P img/ '+mgf)
            bb=bb.replace(imgys, '![img2](img/'+mgf[-40:]+')\n')
        except:
            print("无img")
        try:
            mg = re.search("<img src='", bb,flags=0).span()
            mgg=mg[1]
            mggg=bb[mgg:]
            
            mg2 = re.search("' />", mggg,flags=0).span()
            mg22=mg2[0]
            mgf=mggg[:mg22]
            print("文章内图像:"+mgf)
            imgys="<img src='"+mgf+"' />"
            os.system('wget -P img/ '+mgf)
            bb=bb.replace(imgys, '![img3](img/'+mgf[-40:]+')\n')
        except:
            print("无img")
        try:
            mg = re.search("<img src='", bb,flags=0).span()
            mgg=mg[1]
            mggg=bb[mgg:]
            
            mg2 = re.search("' />", mggg,flags=0).span()
            mg22=mg2[0]
            mgf=mggg[:mg22]
            print("文章内图像:"+mgf)
            imgys="<img src='"+mgf+"' />"
            os.system('wget -P img/ '+mgf)
            bb=bb.replace(imgys, '![img4](img/'+mgf[-40:]+')\n')
        except:
            print("无img")
        try:
            mg = re.search("<img src='", bb,flags=0).span()
            mgg=mg[1]
            mggg=bb[mgg:]
            
            mg2 = re.search("' />", mggg,flags=0).span()
            mg22=mg2[0]
            mgf=mggg[:mg22]
            print("文章内图像:"+mgf)
            imgys="<img src='"+mgf+"' />"
            os.system('wget -P img/ '+mgf)
            bb=bb.replace(imgys, '![img5](img/'+mgf[-40:]+')\n')
        except:
            print("无img")
        try:
            u=re.search("<img id='vipImage' src='/ajax/ashx/common.ashx?",bb).span()
            bbv=u[1]
            bbvv=bb[bbv:]
            n=re.search("' />",bbvv).span()
            bvvv=n[0]
            bvv=bbvv[:bvvv]
            picurl='http://book.sfacg.com/ajax/ashx/common.ashx'+bvv
            vimgys="<img id='vipImage' src='/ajax/ashx/common.ashx"+bvv+"' />"
            pi=requests.get(picurl, headers=headers, cookies=cookies).content
            saveimg("vimg/"+title_without_md+".gif", pi)
            os.system("ffmpeg -i "+"\""+"vimg/"+title_without_md+".gif\" "+"\""+"vimg/"+title_without_md+".png\"")
            bb=bb.replace(vimgys, '![vimg](vimg/'+title_without_md+'.png)\n')
            os.system("rm \"vimg/"+title_without_md+".gif\"")
            ret=Title+Author+UPDate_time+Count_num+"\n***\n"
            ret=ret+"&nbsp;"+bb
            save(title_without_md+".md", ret)
            return ret
        except:
            print("无VIPimg")
        ret=Title+Author+UPDate_time+Count_num+"\n***\n"
        ret=ret+"&nbsp;"+bb
        save(title_without_md+".md", ret)
        return ret
    except:
        return "获取失败"
def manual(url):
    while 1:
        print(sf(url))
        tj = input("是否继续? ,下一章输入n,上一章输入l,重输链接输入r ")
        if tj == "n":
            url=sfnext(url)
        if tj == "l":
            url=sflast(url)
        if tj == "r":
            url=input("请输入SF文章链接:")
def auto(url):
    while 1:
        print(sf(url))
        url=sfnext(url)
import re,os
url=input("请输入SF文章链接:")
mode=input("模式选择:手动模式输入m 自动模式输入a ")
if mode == "m":
    manual(url)
if mode == "a":
    auto(url)
