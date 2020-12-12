import sys
import requests
import xml.etree.ElementTree as ElementTree

ReqUrl = "https://teht.hometax.go.kr/wqAction.do?actionId=ATTABZAA001R08&screenId=UTEABAAA13&popupYn=false&realScreenId="
ReqData = "<map id=\"ATTABZAA001R08\"><pubcUserNo/><mobYn>N</mobYn><inqrTrgtClCd>1</inqrTrgtClCd><txprDscmNo>\{CRN\}</txprDscmNo><dongCode>85</dongCode><psbSearch>Y</psbSearch><map id=\"userReqInfoVO\"/></map><nts<nts>nts>52KhWXziRU1FSh5QaKZ6VNBV3r4kRJ9Wn84THwxB12YCQ41"


def Search_CRN(crn):
    crn = crn.replace("-","")
    res = requests.post(ReqUrl,data=ReqData.replace("\{CRN\}",crn),headers={'Content-Type':'text/xml'})
    xml = ElementTree.fromstring(res.text).findtext("trtCntn")
    result = xml.replace("\n", "").replace("\t", " ")
    return result

result = ""
for idx, value in enumerate(sys.argv):
    if(idx == 0): continue
    result += Search_CRN(value)
