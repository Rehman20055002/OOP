# Encapsulation nedir?
# Melumatlari bir yerde saxlamaq ve 
# xarice qarsi gizli saxlamaq mentiqi ile isleyir.
# Melumatlar sadece xususi metodlar(getter/setter) ile elde edile bilir



# class BankHesabi:
#     def __init__(self, hesab_nomresi, sahibi, ilkin_balans):
#         self.__balans = ilkin_balans
#         self.__hesab_nomresi = hesab_nomresi
#         self.__sahibi = sahibi
#         self._emeliyyat_sayi = 0
#         self.__emeliyyatlar = []
#         print(f"hesab yaradildi: {self.__hesab_nomresi}")
       
#     #    GETTER
#     def get_balans(self):
#         return self.__balans

#     def get_hesab_nomresi(self):
#         return self.__hesab_nomresi

#     def get_sahibi(self):
#         return self.__sahibi

#     # SETTER     Burada args daxil etmeyimizin sebebi meblegin = Yaradilacaq meblege berebaer olmasidir.
#     def pul_yatir(self,mebleg):
#         if mebleg>0:
#             self.__balans+=mebleg
#             self._emeliyyat_sayi+=1
#             self.__emeliyyatlar.append(f"[self._emeliyyat_sayi] Pul yatirildi: {mebleg}")
#             print(f"{mebleg} AZN yatirildi. Yeni balans:{self.__balans} AZN")
#             return True
#         else:
#             print("Mebleg yanlisdir. Daxil edilen mebleg 0-dan asagi ola bilmez")
#             return False

#     def pul_cixart(self, mebleg):
#         if mebleg<=0:
#             print("Mebleg menfi ola bilmez")
#             return False
        
#         if self.__balans<mebleg:
#             print("KIfayet qeder vesait yoxdur.")
#             return False

#         self.__balans-=mebleg
#         self._emeliyyat_sayi+=1
#         self.__emeliyyatlar.append(f"[{self._emeliyyat_sayi}] - {mebleg} AZN cixaris olundu.")
#         print(f"{mebleg} AZN cixaris olundu. Balans: {self.__balans} AZN")


#     def pul_kocur(self, diger_hesab, mebleg):
#         if self.pul_cixart(mebleg):
#             if diger_hesab.pul_yatir(mebleg):
#                 print(f"{mebleg} AZN kocuruldu. => {diger_hesab.get_hesab_nomresi()}")
#                 return True
#         return False

#     def emeliyyatlari_goster(self):
#         print(f"Hesab: {self.__hesab_nomresi} Sahib: {self.__sahibi}")
#         if self.__emeliyyatlar:
#             for emeliyyat in self.__emeliyyatlar:
#                 print(emeliyyat)
#         else:
#             print("Hesabda emeliyyat yoxdur")


# hesab1 = BankHesabi("AZ001", "Rehman Agazade", 3000)
# hesab2 = BankHesabi("AZ002", "Samir Abdullayev", 7000)

# print(f"{hesab1.get_sahibi()} Balans: {hesab1.get_balans()} AZN")

# hesab1.pul_yatir(1000)
# hesab1.pul_cixart(500)
# hesab1.pul_cixart(9000)    
# hesab1.pul_cixart(-200) 
# hesab1.emeliyyatlari_goster()
# hesab2.pul_kocur(hesab1,3000)
# print(f"{hesab1.get_sahibi()} Balans: {hesab2.get_balans()}")





# Inhertiance nedir?
# Bir classin(parent) basqaa sinife(child) oz xususiyyetlerini ve metodlarini oturmesidir.

# class Isci:
#     sirket_adi = "Compar academy"
#     """Isci sinfi"""
#     def __init__(self, ad, soyad, iscinin_id, iscinin_ise_qebul_tarixi):
#         self.ad = ad
#         self.soyad = soyad
#         self.iscinin_id = iscinin_id
#         self.iscinin_ise_qebul_tarixi = iscinin_ise_qebul_tarixi
#         self.aktiv = True
#         print(f"Isci yaradildi: {self.tam_ad()}")

#     def tam_ad(self):
#         return f"{self.ad} {self.soyad}"

#     def ise_basla(self):
#         print(f"{self.tam_ad()} ise basladi.")

#     def ise_son_ver(self):
#         self.aktiv = False
#         print(f"{self.tam_ad()} isden cixdi.")

#     def melumati_goster(self):
#         print(f"Isci ID : {self.iscinin_id}")
#         print(f"Ad, Soyad : {self.tam_ad()}")
#         print(f"Iscinin ise baslama tarixi : {self.iscinin_ise_qebul_tarixi}")
#         print(f"Sirketin adi : {self.sirket_adi}")
#         print(f"Aktivlik : {"Aktiv" if self.aktiv else "Deaktiv"}")


# class Proqramci(Isci):
#     def __init__(self, ad, soyad, iscinin_id, iscinin_ise_qebul_tarixi, proqramramlasdirma_dilleri, tecrube_ili):
#         super().__init__(ad, soyad, iscinin_id, iscinin_ise_qebul_tarixi)
#         self.proqramlasdirma_dilleri = proqramramlasdirma_dilleri
#         self.tecrube_ili = tecrube_ili
#         self.proyektler = []

#     def kod_yaz(self, proyekt_adi):
#         print(f"{self.tam_ad()} '{proyekt_adi}' proyektinde kod yazir....")
#         self.proyektler.append(proyekt_adi)

#     def melumati_goster(self):
#         super().melumati_goster()
#         print(f"Vezife: Proqramci")
#         print(f"Diller:{",".join(self.proqramlasdirma_dilleri)}")
#         print(f"Tecrube ili: {self.tecrube_ili}")
#         print(f"Proyektler : {len(self.proyektler)} eded")



# class Menecer(Isci):
#     def __init__(self, ad, soyad, iscinin_id, iscinin_ise_qebul_tarixi,komanda_hecmi):
#         super().__init__(ad, soyad, iscinin_id, iscinin_ise_qebul_tarixi)
#         self.komanda_hecmi = komanda_hecmi
#         self.komanda = []

#     def komandaya_elave_et(self, isci):
#         if (len(self.komanda)<self.komanda_hecmi):
#             self.komanda.append(isci)
#             print(f"{isci.tam_ad()} menecerin komandasina elave edildi.")
#             print(f"Menecer : {self.tam_ad()}")
#         else:
#             print(F"Komanda hecmi dolub. Max hecm : {self.komanda_hecmi}")

#     def gorus_teskil_et(self):
#         print(f"{self.tam_ad()} gorus teskil edir.")
#         print(f"Istirakcilar : {len(self.komanda)} nefer.")
#         for isci in self.komanda:
#             print(f"Isci - {isci.tam_ad()}")


#     def melumati_goster(self):
#         super().melumati_goster()
#         print(f"Vezife : Menecer")
#         print(f"Komanda hecmi : {self.komanda_hecmi}")
#         print(f"Komanda : {len(self.komanda)}")


    
# class Dizayner(Isci):
#     def __init__(self, ad, soyad, iscinin_id, iscinin_ise_qebul_tarixi, istifade_etdiyi_proqramlar):
#         super().__init__(ad, soyad, iscinin_id, iscinin_ise_qebul_tarixi)
#         self.istifade_etdiyi_proqramlar = istifade_etdiyi_proqramlar
#         self.dizaynlar = []

#     def dizayn_yarat(self, proyekt_adi):
#         print(f"{self.tam_ad()} '{proyekt_adi}' proyektinde dizayn edir.")
#         self.dizaynlar.append(proyekt_adi)

#     def melumati_goster(self):
#         super().melumati_goster()
#         print(f"Vezife : Dizayner")
#         print(f"Proqramlar : {",".join(self.istifade_etdiyi_proqramlar)}")
#         print(f"Dizaynlar : {len(self.dizaynlar)} eded")



# proqramci1 = Proqramci("Rehman", "Aghazade", "C001", "2020-05-10", ["Python", "Javascript"], 3)
# proqramci2 = Proqramci("Orxan", "Allahyarov", "C002", "2019-03-15", ["Java", "C#"], 5)
# menecer = Menecer("Aysel", "Mammadova", "M001", "2018-01-20", 5)
# dizayner = Dizayner("Leyla", "Quliyeva", "D001", "2017-07-19", ["Photoshop", "Illustrator"])

# proqramci1.kod_yaz("E-commerce sayti")
# proqramci2.kod_yaz("Mobil tetbiq")
# dizayner.dizayn_yarat("Brend kimliyi")
# dizayner.dizayn_yarat("Mobil dizayn")
# menecer.komandaya_elave_et(proqramci1)
# menecer.komandaya_elave_et(proqramci2)
# menecer.komandaya_elave_et(dizayner)
# menecer.gorus_teskil_et()

# proqramci1.melumati_goster()
# proqramci2.melumati_goster()
# menecer.melumati_goster()
# dizayner.melumati_goster()

 




#  Polymorphism nedir?
#  EYyni methodun ferqli sinifler ucun ferqli sekilde islemesi demekdir.


# from abc import ABC, abstractmethod
# import math

# class OdenisYontemi(ABC):
#     def __init__(self, sahibi):
#         self.sahibi = sahibi
#     @abstractmethod
#     def odeme_et(self, mebleg):
#         pass
#     def qebzi_cap_et(self, mebleg):
#         print(f"Qebz: {self.sahibi} - {mebleg} AZN odendi")


# class KreditKarti(OdenisYontemi):
#     def __init__(self, sahibi, kart_nomresi, son_istifade_tarixi, cvv):
#         super().__init__(sahibi)
#         self.kart_nomresi = kart_nomresi
#         self.son_istifade_tarixi = son_istifade_tarixi
#         self.__cvv = cvv

#     def odeme_et(self, mebleg):
#         print("Kredit karti ile odenis olundu.")
#         print(f"Kart nomresi : **** **** **** {self.kart_nomresi[-4:]}")
#         print(f"Mebleg : {mebleg} AZN")
#         print("Odenis ugurlu kecdi")
#         self.qebzi_cap_et(mebleg)
#         return True


# class NagdPul(OdenisYontemi):
#     def odeme_et(self, mebleg):
#         print("Odenis nagd sekilde qebul olundu.")
#         print(f"Mebleg : {mebleg} AZN")
#         print("Odenis ugurla heyata kecdi.")
#         self.qebzi_cap_et(mebleg)
#         return True


# class MobilOdenis(OdenisYontemi):
#     def __init__(self, sahibi, mobil_nomresi, operator):
#         super().__init__(sahibi)
#         self.mobil_nomresi = mobil_nomresi
#         self.operator = operator

#     def odeme_et(self, mebleg):
#         print("Odenis mobil sekilde heyata kecdi.")
#         print(f"Kart nomresi : {self.mobil_nomresi}")
#         print(f"Operator : {self.operator}")
#         print(f"Mebleg: {mebleg}")
#         print("Odenis ugurla heyata kecdi.")
#         self.qebzi_cap_et(mebleg)
#         return True


# class KriptoValyuta(OdenisYontemi):
#     def __init__(self, sahibi, wallet_adress, crypto_type):
#         super().__init__(sahibi)
#         self.wallet_adress = wallet_adress
#         self.crypto_type = crypto_type

#     def odeme_et(self, mebleg):
#         print("Odenis kripto il heyata kecdi.")
#         print(f"Wallet Adress : {self.wallet_adress}")
#         print(f"Crypto Type : {self.crypto_type}")
#         print(f"Mebleg: {mebleg}")
#         print("Odenis ugurla heyata kecdi.")
#         self.qebzi_cap_et(mebleg)
#         return True

# def odemeni_prosess_et(odenis_yontemi, mebleg):
#     print("Odeme prosesi baslayir..")
#     print(f"Muster : {odenis_yontemi.sahibi}")
#     return odenis_yontemi.odeme_et(mebleg)


# kart=KreditKarti("Ramin Hidayetov","1234567812345678","12/25","123")
# nagd=NagdPul("Orxan Allahyarov")
# mobil=MobilOdenis("Aysel Mammadova","+994501234567","Azercell")
# kripto=KriptoValyuta("Leyla Quliyeva","1A2B3C4D5E6F7G8H9I0J","Bitcoin")

# odemeni_prosess_et(kart, 150)
# print("-----")
# odemeni_prosess_et(nagd, 75)
# print("-----")
# odemeni_prosess_et(mobil, 200)
# print("-----")
# odemeni_prosess_et(kripto, 500)




# ----------------------------Super ve MRO - Method Resolution Order nedir?--------------------------------------------------
# ---SUPER----
# class Heyvan:
#     def __init__(self, ad):
#         self.ad = ad
#     def ye(self):
#         print(f"{self.ad} yemek yeyir.")

# class It(Heyvan):
#     def __init__(self, ad, cins):
#         super().__init__(ad)
#         self.cins = cins
#     def ye(self):
#         super().ye()
#         print(f"{self.ad} qurugunu bulayir")

# it = It("Linda", "Doberman")
# it.ye()


# ----MRO----

# class Baba:
#     def salamlama(self):
#         print("Baba; Salam balaca.")

# class Ata(Baba):
#     def salamlama(self):
#         print("Ata: Salam oglum")

# class Usaq(Ata):
#         pass  #salamlama metodu yoxdur


# usaq = Usaq()
# usaq.salamlama()



# class Ana:
#     def melumat(self):
#         print("Ana: Yemek hazirdir!")

# class Ata:
#     def melumat(self):
#         print("Ata: Pul verdim!")

# class Usaq(Ata,Ana):
#     pass


# usaq = Usaq()
# usaq.melumat()



# class Ana:
#     def __init__(self,ad):
#         self.ad = ad

# class Usaq(Ana):
#     def __init__(self,ad,yas):
#         super().__init__(ad)
#         self.yas = yas


# usaq = Usaq("Ramin" 18)
# print(usaq.ad)



# class X:
#     def show(self):
#         print("X")

# class Y(X):
#     def show(self):
#         print("Y")
#         super().show()

# class Z(X):
#     def show(self):
#         print("Z")
#         super().show()

# class A(Y):
#     def show(self):
#         print("A")
#         super().show()

# class B(Z):
#     def show(self):
#         print("B")
#         super().show()

# class C(A,B):
#     def show(self):
#         print("C")
#         super().show()

# class F(X):
#     def show(self):
#         print("F")
#         super().show()

# class O(X):
#     def show(self):
#         print("O")
#         super().show()

# class D(C,F,O):
#     def show(self):
#         print("D")
#         super().show()

# class End:
#     def show(self):
#         pass

# X._bases_=(End,)

# d=D()
# print(D.mro())
# d.show()




# # -------------------ABSTRACTION nedir?-------------------------------------

# # Musteri gorur: icki_hazirla()
# # Musteri gormur: daxili_prosesler()




# from abc import ABC, abstractmethod
# # Asagidakilar musterinin gormediyi terefidir
# class IckiAparati(ABC):
#     def __init__(self,ad):
#         self.ad = ad
#         print(f"{ad} aparati hazirdir")

#     @abstractmethod
#     def _mehsul_hazirla(self):                      
#         pass

#     @abstractmethod
#     def _bisir(self):
#         pass

#     @abstractmethod
#     def _fincan_doldur(self):
#         pass

# # Indi public metodu ile musterinin gorduyu terefi yazirirq

#     def icki_hazirla(self, boyuk_olsun=False):
#         olcu = "Boyuk" if boyuk_olsun else "Kicik"
#         print(f"{olcu} {self.ad} hazirlanir")

#         # daxili prosesler
#         self._mehsul_hazirla()
#         self._bisir()
#         self._fincan_doldur()
#         print(f"{self.ad} hazirdir. Nus olsun!")


# class KofeAparati(IckiAparati):
#     def _mehsul_hazirla(self):
#         print("Kofe denleri uyudulur")
#     def _bisir(self):
#         print("Kofe demlenir")
#     def _fincan_doldur(self):
#         print("Fincana tokulur")


# class CayAparati(IckiAparati):
#     def _mehsul_hazirla(self):
#         print("Cay yarpaqlari hazirlanir")
#     def _bisir(self):
#         print("Cay demlenir")
#     def _fincan_doldur(self):
#         print("Fincana tokulur")


# class KakaoAparati(IckiAparati):
#     def _mehsul_hazirla(self):
#         print("Kokao tozu hazirlanir")
#     def _bisir(self):
#         print("Kofe qarisdirilir")
#     def _fincan_doldur(self):
#         print("Fincana tokulur")

# kofe_aparati = KofeAparati("ESpresso")
# cay_aparati = CayAparati("Early Grey")
# kakao_aparati = KakaoAparati("Hot Chocolate")

# kofe_aparati.icki_hazirla(boyuk_olsun=True)
# cay_aparati.icki_hazirla()
# kakao_aparati.icki_hazirla()


