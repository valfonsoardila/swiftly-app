from typing import Any, Optional
from .guide import Guide
from .recipient import Recipient
class File:
    def __init__(self,id, year: int, month: int):
        self.__id = id
        self.__year = year
        self.__month = month
        self.__guideList = list[Guide] = []


    def getId(self)->str:
        return self.__id
    
    def setId(self, id: str):
        self.__id = id
    
    def getYear(self) -> int:
        return self.__year

    def setYear(self, year: int):
        self.__year = year

    def getMonth(self) -> int:
        return self.__month

    def setMonth(self, month: int):
        self.__month = month

    def getGuideList(self):
        return self.__guideList

    def addGuide(self, guide: Guide):
        self.__guideList.append(guide)

    def searchGuideByNumber(self, guideNumber: str) -> Optional[Guide]:
        for guide in self.__guideList:
            if guide.getGuideNumber() == guideNumber:
                return guide
        return None

    def searchGuidesByRecipient(self, recipient: Recipient) -> list[Guide]:
        return [
            guide for guide in self.__guideList if guide.getRecipient() == recipient
        ]

    def toJson(self):
        return {
            "year": self.__year,
            "month": self.__month,
            "guide_list": [guide.toJson() for guide in self.__guideList],
        }

    @staticmethod
    def fromJson(data):
        guide_list = [
            Guide.fromJson(guide_data) for guide_data in data.get("guide_list", [])
        ]
        file = File(
            data.get("file_id"), data.get("year"), data.get("month"), guide_list
        )
        return file
