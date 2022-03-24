import pytest
from liste import *

dieListe: ListeIterativ[int] = ListeIterativ()

def pruefeListenInhalt(dieListe: Liste[int], erwartet: list[int]):
        if len(erwartet) == 0:
            assert dieListe.ist_leer()
        else:
            assert not dieListe.ist_leer()
        assert len(erwartet) == len(dieListe)
        for i in range(0,len(erwartet)):
            assert erwartet[i] == dieListe[i]

def test_1_1():
        assert dieListe.ist_leer()
        dieListe.anhaengen(719)
        pruefeListenInhalt(dieListe, [719])

        assert 84 not in dieListe
        dieListe.anhaengen(320)
        pruefeListenInhalt(dieListe, [719,320])

        assert 719 in dieListe
        assert 719 in dieListe
        assert 375 not in dieListe
        assert 691 not in dieListe
        dieListe.anhaengen(112)
        pruefeListenInhalt(dieListe, [719,320,112])

        dieListe.anhaengen(646)
        pruefeListenInhalt(dieListe, [719,320,112,646])

        dieListe.anhaengen(608)
        pruefeListenInhalt(dieListe, [719,320,112,646,608])

        assert 408 not in dieListe
        dieListe.anhaengen(718)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718])

        dieListe.anhaengen(726)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726])

        assert 267 not in dieListe
        assert 112 in dieListe
        dieListe.anhaengen(241)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241])

        assert 646 in dieListe
        dieListe.anhaengen(536)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536])

        dieListe.anhaengen(297)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297])

        assert 21 not in dieListe
        dieListe.anhaengen(290)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290])

        dieListe.anhaengen(534)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534])

        assert 4 not in dieListe
        assert 718 in dieListe
        assert 710 not in dieListe
        dieListe.anhaengen(671)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671])

        dieListe.anhaengen(871)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871])

        dieListe.anhaengen(986)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986])

        dieListe.anhaengen(958)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958])

        assert 534 in dieListe
        assert 646 in dieListe
        dieListe.anhaengen(98)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98])

        assert 98 in dieListe
        assert 320 in dieListe
        assert 671 in dieListe
        assert 719 in dieListe
        assert 112 in dieListe
        assert 608 in dieListe
        assert 986 in dieListe
        assert 608 in dieListe
        dieListe.anhaengen(102)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102])

        dieListe.anhaengen(19)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19])

        assert 986 in dieListe
        dieListe.anhaengen(126)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126])

        dieListe.anhaengen(771)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771])

        assert 5 not in dieListe
        dieListe.anhaengen(780)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780])

        dieListe.anhaengen(226)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226])

        assert 290 in dieListe
        assert 8 not in dieListe
        dieListe.anhaengen(936)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226,936])

        assert 357 not in dieListe
        assert 241 in dieListe
        dieListe.anhaengen(986)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226,936,986])

        dieListe.anhaengen(335)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226,936,986,335])

        dieListe.anhaengen(40)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226,936,986,335,40])

        dieListe.anhaengen(441)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226,936,986,335,40,441])

        dieListe.anhaengen(254)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226,936,986,335,40,441,254])

        assert 580 not in dieListe
        dieListe.anhaengen(526)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226,936,986,335,40,441,254,526])

        dieListe.anhaengen(820)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226,936,986,335,40,441,254,526,820])

        dieListe.anhaengen(528)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226,936,986,335,40,441,254,526,820,528])

        assert 62 not in dieListe
        assert 986 in dieListe
        dieListe.anhaengen(340)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226,936,986,335,40,441,254,526,820,528,340])

        dieListe.anhaengen(731)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226,936,986,335,40,441,254,526,820,528,340,731])

        dieListe.anhaengen(704)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226,936,986,335,40,441,254,526,820,528,340,731,704])

        assert 242 not in dieListe
        assert 70 not in dieListe
        assert 526 in dieListe
        dieListe.anhaengen(967)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226,936,986,335,40,441,254,526,820,528,340,731,704,967])

        assert 731 in dieListe
        assert 229 not in dieListe
        assert 936 in dieListe
        assert 241 in dieListe
        assert 764 not in dieListe
        dieListe.anhaengen(83)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226,936,986,335,40,441,254,526,820,528,340,731,704,967,83])

        assert 646 in dieListe
        assert 544 not in dieListe
        dieListe.anhaengen(308)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226,936,986,335,40,441,254,526,820,528,340,731,704,967,83,308])

        assert 528 in dieListe
        dieListe.anhaengen(254)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226,936,986,335,40,441,254,526,820,528,340,731,704,967,83,308,254])

        assert 464 not in dieListe
        assert 468 not in dieListe
        assert 986 in dieListe
        dieListe.anhaengen(794)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226,936,986,335,40,441,254,526,820,528,340,731,704,967,83,308,254,794])

        dieListe.anhaengen(217)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226,936,986,335,40,441,254,526,820,528,340,731,704,967,83,308,254,794,217])

        assert 333 not in dieListe
        dieListe.anhaengen(210)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226,936,986,335,40,441,254,526,820,528,340,731,704,967,83,308,254,794,217,210])

        dieListe.anhaengen(65)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226,936,986,335,40,441,254,526,820,528,340,731,704,967,83,308,254,794,217,210,65])

        dieListe.anhaengen(415)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226,936,986,335,40,441,254,526,820,528,340,731,704,967,83,308,254,794,217,210,65,415])

        dieListe.anhaengen(793)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226,936,986,335,40,441,254,526,820,528,340,731,704,967,83,308,254,794,217,210,65,415,793])

        assert 883 not in dieListe
        assert 463 not in dieListe
        dieListe.anhaengen(551)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226,936,986,335,40,441,254,526,820,528,340,731,704,967,83,308,254,794,217,210,65,415,793,551])

        assert 958 in dieListe
        dieListe.anhaengen(368)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226,936,986,335,40,441,254,526,820,528,340,731,704,967,83,308,254,794,217,210,65,415,793,551,368])

        dieListe.anhaengen(466)
        pruefeListenInhalt(dieListe, [719,320,112,646,608,718,726,241,536,297,290,534,671,871,986,958,98,102,19,126,771,780,226,936,986,335,40,441,254,526,820,528,340,731,704,967,83,308,254,794,217,210,65,415,793,551,368,466])

        assert 780 in dieListe
        assert 850 not in dieListe

