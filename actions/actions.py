# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any,Text,Dict,List
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

#skema seputar khs
class aksiGetNama(Action):

    def name(self) -> Text:
        return "aksi_view_khs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        semester = tracker.get_slot("semester")
        if not semester:
            dispatcher.utter_message(text="Maaf tidak dapat memproses, ulangi pertanyaan dengan memasukkan angka semester")
        else:
            dispatcher.utter_message(text=f"ini adalah khs untuk semester {semester}!")
        return []

class aksiGetNama(Action):

    def name(self) -> Text:
        return "aksi_view_sks_khs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        semester = tracker.get_slot("semester")
        if not semester:
            dispatcher.utter_message(text="Maaf tidak dapat memproses, ulangi pertanyaan dengan memasukkan angka semester")
        else:
            dispatcher.utter_message(text=f"ini adalah sks dari khs untuk semester {semester}!")
        return []

class aksiGetNama(Action):

    def name(self) -> Text:
        return "aksi_view_ipk_khs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        semester = tracker.get_slot("semester")
        if not semester:
            dispatcher.utter_message(text="Maaf tidak dapat memproses, ulangi pertanyaan dengan memasukkan angka semester")
        else:
            dispatcher.utter_message(text=f"ini adalah ipk dari khs untuk semester {semester}!")
        return []

class aksiGetNama(Action):

    def name(self) -> Text:
        return "aksi_view_ip_khs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        semester = tracker.get_slot("semester")
        if not semester:
            dispatcher.utter_message(text="Maaf tidak dapat memproses, ulangi pertanyaan dengan memasukkan angka semester")
        else:
            dispatcher.utter_message(text=f"ini adalah ip dari khs untuk semester {semester}!")
        return []

class aksiGetNama(Action):

    def name(self) -> Text:
        return "aksi_view_sp_khs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        semester = tracker.get_slot("semester")
        if not semester:
            dispatcher.utter_message(text="Maaf tidak dapat memproses, ulangi pertanyaan dengan memasukkan angka semester")
        else:
            dispatcher.utter_message(text=f"ini adalah khs dari sp untuk semester {semester}!")
        return []

#skema seputar krs
class aksiGetNama(Action):

    def name(self) -> Text:
        return "aksi_view_krs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        semester = tracker.get_slot("semester")
        if not semester:
            dispatcher.utter_message(text="Maaf tidak dapat memproses, ulangi pertanyaan dengan memasukkan angka semester")
        else:
            dispatcher.utter_message(text=f"ini adalah krs untuk semester {semester}!")
        return []

class aksiGetNama(Action):

    def name(self) -> Text:
        return "aksi_view_sks_krs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        semester = tracker.get_slot("semester")
        if not semester:
            dispatcher.utter_message(text="Maaf tidak dapat memproses, ulangi pertanyaan dengan memasukkan angka semester")
        else:
            dispatcher.utter_message(text=f"ini adalah jumlah sks krs yang diambil untuk semester {semester}!")
        return []

class aksiGetNama(Action):

    def name(self) -> Text:
        return "aksi_view_max_sks_krs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        semester = tracker.get_slot("semester")
        if not semester:
            dispatcher.utter_message(text="Maaf tidak dapat memproses, ulangi pertanyaan dengan memasukkan angka semester")
        else:
            dispatcher.utter_message(text=f"ini adalah jumlah maksimum sks yang dapat diambil untuk semester {semester}!")
        return []

class aksiGetNama(Action):

    def name(self) -> Text:
        return "aksi_view_jadwal_mk_krs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mk = tracker.get_slot("mk")
        if not mk:
            dispatcher.utter_message(text="Maaf tidak dapat memproses, ulangi pertanyaan dengan memasukkan nama mata kuliah")
        else:
            dispatcher.utter_message(text=f"ini adalah jadwal untuk mata kuliah  {mk}!")
        return []

class aksiGetNama(Action):

    def name(self) -> Text:
        return "aksi_view_dosen_mk_krs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mk = tracker.get_slot("mk")
        if not mk:
            dispatcher.utter_message(text="Maaf tidak dapat memproses, ulangi pertanyaan dengan memasukkan nama mata kuliah")
        else:
            dispatcher.utter_message(text=f"ini adalah nama dosen yang mengampu mata kuliah  {mk}!")
        return []

class aksiGetNama(Action):

    def name(self) -> Text:
        return "aksi_aksi_view_ruangan_mk_krs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mk = tracker.get_slot("mk")
        if not mk:
            dispatcher.utter_message(text="Maaf tidak dapat memproses, ulangi pertanyaan dengan memasukkan nama mata kuliah")
        else:
            dispatcher.utter_message(text=f"ini adalah ruangan untuk mata kuliah  {mk}!")
        return []

class aksiGetNama(Action):

    def name(self) -> Text:
        return "aksi_view_sks_mk_krs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mk = tracker.get_slot("mk")
        if not mk:
            dispatcher.utter_message(text="Maaf tidak dapat memproses, ulangi pertanyaan dengan memasukkan nama mata kuliah")
        else:
            dispatcher.utter_message(text=f"ini adalah jumlah sks dari mata kuliah  {mk}!")
        return []

class aksiGetNama(Action):

    def name(self) -> Text:
        return "aksi_view_kode_mk_krs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mk = tracker.get_slot("mk")
        if not mk:
            dispatcher.utter_message(text="Maaf tidak dapat memproses, ulangi pertanyaan dengan memasukkan nama mata kuliah")
        else:
            dispatcher.utter_message(text=f"ini adalah kode dari mata kuliah  {mk}!")
        return []

class aksiGetNama(Action):

    def name(self) -> Text:
        return "aksi_view_avaible_mk_krs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        semester = tracker.get_slot("semester")
        if not semester:
            dispatcher.utter_message(text="Maaf tidak dapat memproses, ulangi pertanyaan dengan memasukkan angka semester")
        else:
            dispatcher.utter_message(text=f"ini adalah list mata kuliah yang dapat diambil pada semester  {semester}!")
        return []

class aksiGetNama(Action):

    def name(self) -> Text:
        return "aksi_view_avaible_mk_sp_krs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        semester = tracker.get_slot("semester")
        if not semester:
            dispatcher.utter_message(text="Maaf tidak dapat memproses, ulangi pertanyaan dengan memasukkan angka semester")
        else:
            dispatcher.utter_message(text=f"ini adalah list mata kuliah yang dapat diambil pada semester  {semester}!")
        return []

class aksiGetNama(Action):

    def name(self) -> Text:
        return "aksi_view_max_sks_sp_krs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        semester = tracker.get_slot("semester")
        if not semester:
            dispatcher.utter_message(text="Maaf tidak dapat memproses, ulangi pertanyaan dengan memasukkan angka semester")
        else:
            dispatcher.utter_message(text=f"ini adalah jumlah maksimum sks yang dapat diambil untuk semester {semester}!")
        return []

class aksiGetNama(Action):

    def name(self) -> Text:
        return "aksi_view_sks_sp_krs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        semester = tracker.get_slot("semester")
        if not semester:
            dispatcher.utter_message(text="Maaf tidak dapat memproses, ulangi pertanyaan dengan memasukkan angka semester")
        else:
            dispatcher.utter_message(text=f"ini adalah jumlah maksimum sks yang dapat diambil untuk semester {semester}!")
        return []

class aksiGetNama(Action):

    def name(self) -> Text:
        return "aksi_view_sks_sp_krs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        semester = tracker.get_slot("semester")
        if not semester:
            dispatcher.utter_message(text="Maaf tidak dapat memproses, ulangi pertanyaan dengan memasukkan angka semester")
        else:
            dispatcher.utter_message(text=f"ini adalah jumlah sks krs yang diambil untuk semester {semester}!")
        return []

class aksiGetNama(Action):

    def name(self) -> Text:
        return "aksi_view_sp_krs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        semester = tracker.get_slot("semester")
        if not semester:
            dispatcher.utter_message(text="Maaf tidak dapat memproses, ulangi pertanyaan dengan memasukkan angka semester")
        else:
            dispatcher.utter_message(text=f"ini adalah krs untuk semester {semester}!")
        return []

#skema seputar transkip nilai
class aksiGetNama(Action):

    def name(self) -> Text:
        return "aksi_view_history_mk_transkip_nilai"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mk = tracker.get_slot("mk")
        if not mk:
            dispatcher.utter_message(text="Maaf tidak dapat memproses, ulangi pertanyaan dengan memasukkan nama mata kuliah")
        else:
            dispatcher.utter_message(text=f"ini adalah history dari mata kuliah {mk}!")
        return []

class aksiGetNama(Action):

    def name(self) -> Text:
        return "aksi_view_nilai_mk_transkip_nilai"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        nilai = tracker.get_slot("nilai")
        if not nilai:
            dispatcher.utter_message(text="Maaf tidak dapat memproses, ulangi pertanyaan dengan memasukkan nilai")
        else:
            dispatcher.utter_message(text=f"ini adalah list mata kuliah dengan nilai {nilai}!")
        return []