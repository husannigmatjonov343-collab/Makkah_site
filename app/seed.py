"""
Ma'lumotlar bazasini boshlang'ich kontent bilan to'ldiruvchi skript.
Ishga tushirish: python -m app.seed

Eslatma: bazada allaqachon kontent bo'lsa, skript hech narsa qilmaydi.
Qayta to'ldirish uchun avval bazani tozalang (masalan, makkah.db faylini o'chiring).
"""
from app.database import SessionLocal, engine, Base
from app.models import Category, Article, UmrahStep, Dua, FAQ


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    if db.query(Category).count() > 0:
        print("Ma'lumotlar bazasida allaqachon kontent mavjud, seed bekor qilindi.")
        db.close()
        return

    # ================= KATEGORIYALAR =================
    cat_tarix = Category(
        slug="tarix", title="Makkai Mukarrama tarixi",
        subtitle="Qadimiy shahardan islom olamining ma'naviy markaziga qadar",
        description=(
            "Ka'baning qurilishidan tortib, bugungi zamonaviy Haram majmuasigacha bo'lgan "
            "necha ming yillik tarixiy yo'l — voqealar, shaxslar va bosqichlar bo'yicha."
        ),
        icon="🕋", order_index=1,
    )
    cat_fazilat = Category(
        slug="fazilatlar", title="Makkaning fazilatlari",
        subtitle="Nima uchun bu shahar musulmonlar uchun eng muqaddas makon",
        description=(
            "Masjidul Haramning, Ka'baning va Makka shahrining diniy ahamiyati, "
            "fazilatlari hamda ularga bog'liq odob-axloq qoidalari haqida."
        ),
        icon="✨", order_index=2,
    )
    db.add_all([cat_tarix, cat_fazilat])
    db.commit()

    # ================= MAQOLALAR: TARIX (6 ta) =================
    tarix_maqolalar = [
        Article(
            category_id=cat_tarix.id, slug="kabaning-qurilishi",
            title="Ka'bai Sharifning qurilishi",
            summary="Ibrohim (a.s.) va Ismoil (a.s.) tomonidan Ka'baning qad ko'tarilishi haqida.",
            quick_fact="Ka'ba balandligi ≈13,1 metr, tomonlari 10-12 metr atrofida.",
            body=(
                "Islomiy rivoyatlarga ko'ra, Ka'baning poydevori juda qadim zamonlarga borib taqaladi, "
                "keyinchalik esa Ibrohim (alayhissalom) o'g'li Ismoil (alayhissalom) bilan birgalikda uni "
                "qayta tiklab, hozirgi ko'rinishiga yaqinlashtirgan. Ka'ba Yer yuzida yagona Yaratganga "
                "ibodat qilish uchun qurilgan birinchi ma'bad sifatida e'zozlanadi.\n\n"
                "Vaqt o'tishi bilan shahar aholisi ko'paygan sari Ka'ba bir necha bor ta'mirlangan — "
                "jumladan, Qurayshlar davrida va Payg'ambarimiz Muhammad (sollallohu alayhi vasallam) "
                "yosh yigit chog'larida sodir bo'lgan mashhur ta'mirlash voqeasi bunga misol bo'ladi. "
                "O'shanda Hajarul Asvadni joyiga qo'yish masalasida qabilalar orasida kelishmovchilik "
                "chiqib, Payg'ambarimiz adolatli yechim topgani tarixiy manbalarda keltiriladi: u kishi "
                "toshni mato ustiga qo'yib, barcha qabila boshliqlariga matoning chetidan ushlab "
                "ko'tarishni buyurgan, so'ng toshni o'z qo'llari bilan joyiga o'rnatgan.\n\n"
                "Keyingi asrlarda ham Ka'ba turli hukmdorlar davrida — jumladan, Abbosiylar va "
                "Usmoniylar davrida — bir necha bor ta'mirlanib, mustahkamlangan. Har safar ta'mirlash "
                "ishlari Ka'baning asl shakli va o'lchamlarini imkon qadar saqlab qolishga qaratilgan."
            ), order_index=1,
        ),
        Article(
            category_id=cat_tarix.id, slug="islomdan-oldingi-makka",
            title="Islomdan oldingi Makka",
            summary="Savdo yo'llari kesishgan nuqtada joylashgan qadimiy shahar hayoti.",
            quick_fact="Makka Yaman-Sham savdo yo'lining markaziy bekati bo'lgan.",
            body=(
                "Islom kelishidan oldin ham Makka Arabiston yarim orolidagi muhim savdo va ziyorat "
                "markazlaridan biri bo'lgan. Shahar quraq va tog'lar orasidagi vodiyda joylashgan bo'lsada, "
                "Zamzam suyi manbai tufayli va yil bo'yi turli qabilalarning Ka'ba atrofida yig'ilib, "
                "savdo-sotiq qilishi tufayli gullab-yashnagan.\n\n"
                "Har yili turli burchaklardan kelgan qabilalar mavsumiy yarmarkalarda uchrashib, "
                "she'riyat musobaqalari o'tkazishgan va mahsulot almashtirishgan. Ukoz kabi mashhur "
                "bozorlarda arab tilining eng go'zal namunalari — qasidalar o'qilgan, g'oliblarning "
                "she'rlari esa Ka'ba devoriga osib qo'yilgan, deya rivoyat qilinadi.\n\n"
                "Bu an'analar Makkani nafaqat diniy, balki madaniy va iqtisodiy jihatdan ham mintaqaning "
                "muhim markaziga aylantirgan. Qurayshlar qabilasi shahar boshqaruvida va savdo "
                "yo'llarini nazorat qilishda yetakchi mavqega ega bo'lgan."
            ), order_index=2,
        ),
        Article(
            category_id=cat_tarix.id, slug="payg'ambar-davri",
            title="Payg'ambarimiz davridagi Makka",
            summary="Vahiy nozil bo'lishi, hijrat va Makkaning fath etilishi.",
            quick_fact="Makka fathi hijriy 8-yilda, deyarli qonsiz amalga oshgan.",
            body=(
                "Makka Muhammad (sollallohu alayhi vasallam)ning tug'ilgan va birinchi vahiy nozil "
                "bo'lgan shahridir. Hiro g'orida boshlangan vahiy jarayoni keyinchalik butun bir "
                "dinning boshlanishiga sabab bo'ldi.\n\n"
                "Dastlabki yillarda musulmonlar ko'plab qiyinchiliklarga duch kelib, keyinchalik "
                "Madinaga hijrat qilishga majbur bo'lishgan. Bu davr Makka tarixida ham, islom "
                "tarixida ham burilish nuqtasi bo'lib qoldi — endi musulmonlar o'z jamoasini erkin "
                "shakllantira oladigan makonga ega bo'lishdi.\n\n"
                "Bir necha yildan so'ng, Makka tinch yo'l bilan fath etilib, Ka'ba butlardan "
                "tozalanib, qaytadan faqat Yaratganga ibodat qilish maskaniga aylantirilgan. "
                "Shu voqeadan so'ng Makka islom olamining ma'naviy markazi sifatidagi maqomini "
                "butun tarix davomida saqlab kelmoqda."
            ), order_index=3,
        ),
        Article(
            category_id=cat_tarix.id, slug="xalifalar-davri",
            title="Xalifalar va sultonlar davrida Makka",
            summary="O'rta asrlarda Haramning kengaytirilishi va boshqaruvi.",
            quick_fact="Abbosiy xalifa Al-Mahdiy davrida Masjidul Haram sezilarli kengaytirilgan.",
            body=(
                "Rashidun xalifalar davridan boshlab, keyinchalik Umaviylar, Abbosiylar, Ayyubiylar, "
                "Mamluklar va Usmoniylar davrida Masjidul Haram muntazam ravishda kengaytirilib, "
                "ta'mirlanib turilgan. Har bir davr o'ziga xos me'moriy iz qoldirgan — ustunlar, "
                "gumbazlar va minoralar shu davrlar yodgorligi sifatida saqlanib qolgan.\n\n"
                "O'rta asrlarda Haj karvonlari — masalan, Damashq va Qohiradan yo'lga chiquvchi "
                "yirik karvonlar — minglab ziyoratchilarni Makkaga olib kelgan. Bu karvonlar yo'lida "
                "suv omborlari, karvonsaroylar qurilib, xavfsizlik ta'minlangan.\n\n"
                "Usmoniylar davrida esa Haram atrofiga qo'shimcha minoralar va gumbazlar qo'shilib, "
                "shahar infratuzilmasi yanada mustahkamlangan. Bu davr yodgorliklarining ba'zilari "
                "hozirgi kungacha muzeylarda saqlanmoqda."
            ), order_index=4,
        ),
        Article(
            category_id=cat_tarix.id, slug="zamonaviy-makka",
            title="Zamonaviy Makka va Masjidul Haramning kengaytirilishi",
            summary="Millionlab ziyoratchilarni qabul qilish uchun amalga oshirilgan katta loyihalar.",
            quick_fact="Kengaytirilgan Masjidul Haram bir vaqtning o'zida millionga yaqin kishini sig'dira oladi.",
            body=(
                "So'nggi o'n yilliklarda har yili Hajga va Umraga keluvchilar soni sezilarli darajada "
                "oshgani sababli, Masjidul Haram bir necha bor kengaytirildi. Zamonaviy infratuzilma — "
                "yo'llar, temir yo'l tizimlari, mehmonxonalar va tavof maydonining kengayishi millionlab "
                "ziyoratchilarga ibodatlarini nisbatan qulayroq bajarishga imkon bermoqda.\n\n"
                "Haram atrofida qurilgan ko'p qavatli qo'shimcha binolar, harakatlanuvchi yo'lkalar va "
                "zamonaviy shamollatish tizimlari issiq iqlim sharoitida ham ziyoratchilarga qulaylik "
                "yaratadi. Shuningdek, Masjidul Haram atrofidagi metro va avtobus tizimlari shaharning "
                "boshqa qismlaridan kelishni osonlashtirgan.\n\n"
                "Shunga qaramay, shahar markazida joylashgan Ka'ba va uning atrofidagi muqaddas makon "
                "asrlar davomida o'zining ma'naviy mohiyatini saqlab qolmoqda — texnologiya rivojlansa-da, "
                "ziyoratchining maqsadi o'zgarmagan holicha qolmoqda."
            ), order_index=5,
        ),
        Article(
            category_id=cat_tarix.id, slug="hijrul-asvad-tarixi",
            title="Hajarul Asvad (Qora tosh) tarixi",
            summary="Ka'ba burchagidagi muqaddas toshning kelib chiqishi va maqomi.",
            quick_fact="Hajarul Asvad hozirda kumush ramka bilan mustahkamlangan holda saqlanadi.",
            body=(
                "Hajarul Asvad — Ka'baning sharqiy burchagiga o'rnatilgan, tarix davomida alohida "
                "e'zozlangan tosh. Ko'plab rivoyatlarga ko'ra, bu tosh jannatdan tushirilgan va "
                "vaqt o'tishi bilan o'z rangini o'zgartirgan, deyiladi.\n\n"
                "Tavof paytida ziyoratchilar imkon bo'lsa uni o'pishga yoki qo'l bilan ishora "
                "qilishga harakat qiladi — bu Payg'ambarimiz sunnatiga ergashish maqsadida "
                "bajariladigan amal, izdihom katta bo'lganda esa uzoqdan ishora qilish kifoya.\n\n"
                "Tarix davomida tosh bir necha marta shikastlangan va qayta tiklangan, "
                "hozirda u bir necha bo'lakdan iborat bo'lib, kumush ramka ichiga mahkamlangan "
                "holda saqlanmoqda."
            ), order_index=6,
        ),
    ]
    db.add_all(tarix_maqolalar)

    # ================= MAQOLALAR: FAZILATLAR (6 ta) =================
    fazilat_maqolalar = [
        Article(
            category_id=cat_fazilat.id, slug="masjidul-haramda-namoz-savobi",
            title="Masjidul Haramda o'qilgan namozning fazilati",
            summary="Boshqa masjidlarga nisbatan berilgan alohida mukofot haqida.",
            quick_fact="Rivoyatlarda Masjidul Haramdagi namoz ming barobar savobli deyiladi.",
            body=(
                "Ko'plab hadis rivoyatlarida Masjidul Haramda o'qilgan namoz boshqa masjidlarda "
                "o'qilgan namozlardan ming barobar ko'proq savobga ega ekanligi bayon qilinadi "
                "(Masjidi Nabaviydan tashqari). Shu sababli dunyoning turli burchaklaridan kelgan "
                "musulmonlar imkon qadar ko'proq vaqtini shu muqaddas maskonda ibodat bilan "
                "o'tkazishga intiladi.\n\n"
                "Bu fazilat ziyoratchilar uchun Umra va Haj safarining ma'naviy qadrini yanada "
                "oshiradi — ko'pchilik besh vaqt namozni Haramda ado etishga, hattoki navbatdagi "
                "namozgacha shu yerda kutib o'tirishga harakat qiladi."
            ), order_index=1,
        ),
        Article(
            category_id=cat_fazilat.id, slug="haram-hududining-muqaddasligi",
            title="Haram hududining muqaddasligi",
            summary="Makka atrofidagi chegaralangan hudud nima uchun alohida hurmatga sazovor.",
            quick_fact="Haram chegaralari shahar markazidan bir necha kilometr uzoqlikda joylashgan.",
            body=(
                "Makka shahri atrofida 'Haram' deb nomlangan chegaralangan hudud mavjud bo'lib, "
                "bu yerda o'simliklarni kesish, yovvoyi hayvonlarni ovlash va janjal-nizo chiqarish "
                "taqiqlanadi. Bu qoidalar Haramning tinchlik va xotirjamlik maskani ekanligini "
                "ta'kidlaydi.\n\n"
                "Ihromga kirgan har bir ziyoratchi ushbu hududga yaqinlashganda alohida ma'naviy "
                "holatga o'tadi va o'zini kundalik tashvishlardan xoli qilishga harakat qiladi. "
                "Haram chegaralarini bildiruvchi maxsus belgi-lavhalar yo'l bo'ylab o'rnatilgan."
            ), order_index=2,
        ),
        Article(
            category_id=cat_fazilat.id, slug="zamzam-suvining-fazilati",
            title="Zamzam suvining fazilati",
            summary="Asrlar osha qurimagan mo''jizaviy buloq haqida.",
            quick_fact="Zamzam quduqi minglab yillardan buyon suv chiqarib kelmoqda.",
            body=(
                "Zamzam - Ka'ba yaqinida joylashgan va asrlar davomida to'xtovsiz suv chiqarib "
                "kelayotgan buloqdir. Rivoyatlarga ko'ra, bu buloq Ismoil (alayhissalom) chaqaloqligida "
                "paydo bo'lgan — onasi Hojar suv izlab Safo va Marva orasida yugurgan lahzalarda.\n\n"
                "Musulmonlar Zamzam suvini ichishda niyat qilib ichishni odat qilishgan, chunki bu "
                "suv qanday niyat bilan ichilsa o'sha maqsad uchun foydali bo'ladi, degan aqida keng "
                "tarqalgan. Bugungi kunda ham millionlab ziyoratchilar Umra va Haj safari davomida "
                "Zamzam suvidan ichib, undan o'zlari bilan olib ketishadi."
            ), order_index=3,
        ),
        Article(
            category_id=cat_fazilat.id, slug="ka'baga-qarab-turish-fazilati",
            title="Ka'baga qarab turishning fazilati",
            summary="Tavof paytidagi va oddiy qarab turishdagi ma'naviy holat.",
            quick_fact="Dunyoning barcha masjidlari namozda Ka'ba tomon yo'naltirilgan.",
            body=(
                "Ko'plab olimlar Ka'baga qarab turishning o'zi ham ibodat hisoblanishini, chunki bu "
                "qalbni Allohni yodga olishga undashini ta'kidlashadi. Har kuni besh vaqt namozda "
                "dunyoning turli burchaklaridagi musulmonlar Ka'ba tomon yuzlanadi, bu esa butun "
                "ummatning birligini ramziy tarzda ifodalaydi.\n\n"
                "Shu bois Masjidul Haramga borgan ziyoratchilar Ka'bani birinchi marta ko'rgan "
                "lahzani hayotlaridagi eng ta'sirli onlardan biri sifatida tasvirlashadi — ko'pchilik "
                "bu lahzada duo qilishga alohida ahamiyat beradi."
            ), order_index=4,
        ),
        Article(
            category_id=cat_fazilat.id, slug="ramazonda-umra-fazilati",
            title="Ramazon oyida Umra qilishning fazilati",
            summary="Yilning boshqa vaqtlariga nisbatan alohida ta'kidlangan mavsum.",
            quick_fact="Ramazonda Umra ayrim rivoyatlarda Hajga tenglashtirilgan savobga ega deyiladi.",
            body=(
                "Hadis ilmida Ramazon oyida ado etilgan Umraning fazilati alohida ta'kidlanadi — "
                "ba'zi rivoyatlarda bu Haj savobiga tenglashtiriladi (garchi Umra Hajning o'rnini "
                "bosmasa-da). Shu sababli har yili Ramazon oyida Makkaga keluvchilar soni sezilarli "
                "darajada ortadi.\n\n"
                "Bu davrda Masjidul Haram tunlari tarovih namozlari va tahajjud ibodatlari bilan "
                "jonlanadi, iftorlik dasturxonlari Haram hovlisida keng yoyiladi. Ziyoratchilar "
                "uchun bu davr ham jismoniy, ham ma'naviy jihatdan tayyorgarlikni talab qiladi, "
                "chunki izdihom odatdagidan ancha yuqori bo'ladi."
            ), order_index=5,
        ),
        Article(
            category_id=cat_fazilat.id, slug="makkada-odob-axloq",
            title="Makkada saqlanishi lozim bo'lgan odob-axloq",
            summary="Muqaddas hududda o'zini tutish bo'yicha umumiy tavsiyalar.",
            quick_fact="Haramda janjal-nizo va gunoh ishlar alohida qat'iylik bilan man etiladi.",
            body=(
                "Makka va Masjidul Haram musulmonlar uchun nafaqat ibodat, balki yuksak odob-axloq "
                "namunasi ko'rsatiladigan makondir. Ziyoratchilardan sabr-toqatli bo'lish, "
                "izdihomda boshqalarga hurmat ko'rsatish va ovozni past tutish talab etiladi.\n\n"
                "Shuningdek, atrof-muhitni toza saqlash, navbatga rioya qilish va boshqa "
                "millat-elat vakillariga mehr-oqibat bilan munosabatda bo'lish — bularning barchasi "
                "Umra va Haj safarining ma'naviy mohiyatini to'ldiruvchi muhim jihatlar hisoblanadi."
            ), order_index=6,
        ),
    ]
    db.add_all(fazilat_maqolalar)
    db.commit()

    # ================= UMRA QADAMLARI (6 ta) =================
    umrah_steps = [
        UmrahStep(
            step_number=1, title="Ihromga kirish (Miqotda niyat qilish)",
            description=(
                "Umra belgilangan chegara — miqotga yetganda boshlanadi. Bu yerda ziyoratchi g'usl "
                "qilib, ihrom kiyimini kiyadi (erkaklar uchun ikki bo'lak tikilmagan oq mato, ayollar "
                "odatdagi hashamatsiz kiyimlarida qoladi) va Umra qilishga niyat qiladi."
            ),
            arabic_text="لَبَّيْكَ اللَّهُمَّ عُمْرَةً",
            transliteration="Labbayka-llohumma 'umratan",
            meaning="Labbayk, Ey Alloh, Umra uchun keldim.",
            tip="Miqotdan o'tishdan oldin ihromga kirish shart, aks holda jarima (fidya) lozim bo'lishi mumkin.",
        ),
        UmrahStep(
            step_number=2, title="Talbiya aytish",
            description=(
                "Ihromga kirgandan so'ng Masjidul Haramga yetib, tavofni boshlaguncha ziyoratchi "
                "yo'l davomida talbiyani ko'p-ko'p takrorlab boradi. Bu zikr Umraning ma'naviy "
                "kayfiyatini his etishga yordam beradi."
            ),
            arabic_text="لَبَّيْكَ اللَّهُمَّ لَبَّيْكَ",
            transliteration="Labbayka-llohumma labbayk",
            meaning="Labbayk, Ey Alloh, mana men huzuringdaman.",
            tip="Talbiyani baland ovozda (ayollar past ovozda) aytish sunnatga muvofiqdir.",
        ),
        UmrahStep(
            step_number=3, title="Ka'ba atrofida tavof qilish",
            description=(
                "Masjidul Haramga kirib, Hajarul Asvad tomondan boshlab Ka'ba atrofida soat "
                "milkiga teskari yo'nalishda yetti marta aylanib chiqiladi. Har bir aylanishda "
                "duo qilish, zikr aytish tavsiya etiladi."
            ),
            tip="Tavof paytida atrofdagi izdihomni hisobga olib, shoshilmasdan, xotirjam harakat qilish tavsiya etiladi.",
        ),
        UmrahStep(
            step_number=4, title="Maqomi Ibrohimda ikki rakat namoz",
            description=(
                "Tavof tugagach, imkon bo'lsa Maqomi Ibrohim yaqinida, aks holda Masjidul Haramning "
                "istalgan qulay joyida ikki rakat namoz o'qish sunnat hisoblanadi."
            ),
            tip="Izdihom katta bo'lsa, bu namozni Masjidul Haramning boshqa burchagida ham o'qish mumkin.",
        ),
        UmrahStep(
            step_number=5, title="Safo va Marva o'rtasida sa'y qilish",
            description=(
                "Safo tepaligidan boshlab Marva tepaligiga qadar yetti marta yurib o'tiladi (4 marta "
                "Safodan Marvaga, 3 marta Marvadan Safoga). Bu Hojar onaning suv izlab yugurgan "
                "voqeasini yodga soladi."
            ),
            arabic_text="إِنَّ الصَّفَا وَالْمَرْوَةَ مِنْ شَعَائِرِ اللَّهِ",
            transliteration="Inna-s-safa wal-marwata min sha'a'irillah",
            meaning="Albatta, Safo va Marva Allohning nishonalaridandir.",
            tip="Erkaklar uchun ikki yashil chiroq oralig'ida tezroq yurish (raml) sunnatdir.",
        ),
        UmrahStep(
            step_number=6, title="Soch oldirish yoki qisqartirish (halq/taqsir)",
            description=(
                "Sa'y tugagach, erkaklar sochini butunlay oldirishi (halq) yoki qisqartirishi "
                "(taqsir) lozim, ayollar esa sochining bir uchidan bir necha santimetr kesishadi. "
                "Shu bilan Umra marosimi nihoyasiga yetadi va ihromdan chiqiladi."
            ),
            tip="Halq (butunlay oldirish) taqsirga (qisqartirishga) nisbatan afzalroq sanaladi.",
        ),
    ]
    db.add_all(umrah_steps)

    # ================= DUOLAR (tag bilan guruhlangan) =================
    duas = [
        Dua(
            slug="talbiya", title="Talbiya duosi", tag="Ihrom",
            occasion="Ihromga kirgandan Ka'bani ko'rgunga qadar takrorlanadi",
            arabic_text="لَبَّيْكَ اللَّهُمَّ لَبَّيْكَ، لَبَّيْكَ لَا شَرِيكَ لَكَ لَبَّيْكَ، إِنَّ الْحَمْدَ وَالنِّعْمَةَ لَكَ وَالْمُلْكَ، لَا شَرِيكَ لَكَ",
            transliteration="Labbayka-llohumma labbayk, labbayka la sharika laka labbayk, inna-l-hamda wa-n-ni'mata laka wal-mulk, la sharika lak",
            translation="Labbayk, Ey Alloh, mana men huzuringdaman, Sening sherikeing yo'q, labbayk. Albatta, hamd, ne'mat va mulk Senga xosdir, Sening sherikeing yo'q.",
            order_index=1,
        ),
        Dua(
            slug="ihromga-kirishda-niyat", title="Ihromga kirishda niyat duosi", tag="Ihrom",
            occasion="G'usl qilib, ihrom kiyimini kiygandan so'ng",
            arabic_text="اللَّهُمَّ إِنِّي أُرِيدُ الْعُمْرَةَ فَيَسِّرْهَا لِي وَتَقَبَّلْهَا مِنِّي",
            transliteration="Allohumma inni uridu-l-'umrata fa yassirha li wa taqabbalha minni",
            translation="Ey Alloh, men Umra qilishni niyat qildim, uni men uchun oson qilgin va uni mendan qabul qilgin.",
            order_index=2,
        ),
        Dua(
            slug="hajarul-asvad-oldida", title="Hajarul Asvad yoniga yetganda o'qiladigan takbir", tag="Tavof",
            occasion="Tavofni boshlashda va har aylanishda Hajarul Asvad tomon yetganda",
            arabic_text="بِسْمِ اللَّهِ، اللَّهُ أَكْبَرُ",
            transliteration="Bismillah, Allohu akbar",
            translation="Alloh nomi bilan boshlayman, Alloh eng ulug'dir.",
            order_index=3,
        ),
        Dua(
            slug="ruknul-yamoniy-va-hajarul-asvad-orasida",
            title="Ruknul Yamoniy bilan Hajarul Asvad orasida o'qiladigan duo", tag="Tavof",
            occasion="Tavofning har bir aylanishida shu ikki burchak orasida",
            arabic_text="رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً وَفِي الْآخِرَةِ حَسَنَةً وَقِنَا عَذَابَ النَّارِ",
            transliteration="Rabbana atina fid-dunya hasanatan wa fil-akhirati hasanatan wa qina 'adhaban-nar",
            translation="Ey Robbimiz, bizga bu dunyoda ham, oxiratda ham yaxshilik ber va bizni do'zax azobidan asra.",
            order_index=4,
        ),
        Dua(
            slug="maqomi-ibrohimda", title="Maqomi Ibrohim yonida o'qiladigan oyat ma'nosi", tag="Tavof",
            occasion="Tavofdan so'ng ikki rakat namozga turishdan oldin",
            arabic_text="وَاتَّخِذُوا مِنْ مَقَامِ إِبْرَاهِيمَ مُصَلًّى",
            transliteration="Wattakhidhu min maqami Ibrahima musalla",
            translation="Va Ibrohimning turgan joyini namozgoh qilib oling.",
            order_index=5,
        ),
        Dua(
            slug="safo-tepaligida", title="Safo va Marvaga chiqishda o'qiladigan duo", tag="Sa'y",
            occasion="Sa'yni boshlashdan oldin, Safo tepaligida",
            arabic_text="إِنَّ الصَّفَا وَالْمَرْوَةَ مِنْ شَعَائِرِ اللَّهِ، أَبْدَأُ بِمَا بَدَأَ اللَّهُ بِهِ",
            transliteration="Inna-s-safa wal-marwata min sha'a'irillah, abda'u bima bada'allohu bih",
            translation="Albatta, Safo va Marva Allohning nishonalaridandir. Men ham Alloh boshlagan narsadan boshlayman.",
            order_index=6,
        ),
        Dua(
            slug="yashil-chiroqlar-orasida", title="Sa'y paytida (yashil chiroqlar orasida) o'qiladigan duo", tag="Sa'y",
            occasion="Sa'yning har bir marotabasida, tez yurish qismida",
            arabic_text="رَبِّ اغْفِرْ وَارْحَمْ إِنَّكَ أَنْتَ الْأَعَزُّ الْأَكْرَمُ",
            transliteration="Rabbi-ghfir warham innaka anta-l-a'azzu-l-akram",
            translation="Ey Robbim, mag'firat qil va rahm qil, albatta Sen eng qudratli va eng karam egasisan.",
            order_index=7,
        ),
        Dua(
            slug="zamzam-ichishda", title="Zamzam suvini ichishda niyat", tag="Ziyorat",
            occasion="Zamzam suvini ichishdan oldin",
            arabic_text="اللَّهُمَّ إِنِّي أَسْأَلُكَ عِلْمًا نَافِعًا وَرِزْقًا وَاسِعًا وَشِفَاءً مِنْ كُلِّ دَاءٍ",
            transliteration="Allohumma inni as'aluka 'ilman nafi'an wa rizqan wasi'an wa shifa'an min kulli da'",
            translation="Ey Alloh, Sendan foydali ilm, keng rizq va har qanday dardan shifo so'rayman.",
            order_index=8,
        ),
        Dua(
            slug="haramdan-chiqishda", title="Masjidul Haramdan chiqishda o'qiladigan duo", tag="Ziyorat",
            occasion="Har safar Masjidul Haramdan tashqariga chiqishda",
            arabic_text="اللَّهُمَّ إِنِّي أَسْأَلُكَ مِنْ فَضْلِكَ",
            transliteration="Allohumma inni as'aluka min fadlik",
            translation="Ey Alloh, Sendan fazlu karamingdan so'rayman.",
            order_index=9,
        ),
    ]
    db.add_all(duas)

    # ================= FAQ (tag bilan guruhlangan) =================
    faqs = [
        FAQ(
            question="Umra bilan Haj o'rtasidagi farq nima?", tag="Umumiy",
            answer=(
                "Haj yiliga bir marta, belgilangan kunlarda bajariladigan va Islomning beshta "
                "asosidan biri hisoblangan farz ibodat, Umra esa yil davomida istalgan vaqtda "
                "bajarilishi mumkin bo'lgan, kichikroq amallardan iborat sunnat ziyoratdir."
            ), order_index=1,
        ),
        FAQ(
            question="Umrani yilning istalgan vaqtida ado etsa bo'ladimi?", tag="Umumiy",
            answer=(
                "Ha, Umra Hajdan farqli o'laroq yil davomida istalgan kunda ado etilishi mumkin, "
                "faqat Haj kunlarida (Zul-hijja oyining muayyan kunlarida) ba'zi cheklovlar bo'lishi mumkin."
            ), order_index=2,
        ),
        FAQ(
            question="Umrani necha marta bajarish mumkin?", tag="Umumiy",
            answer=(
                "Umrani bir necha marta ado etishga shariy jihatdan cheklov yo'q, biroq ba'zi "
                "mamlakatlar vizasi va mahalliy qoidalar bir tashrif davomida takroriy Umra "
                "sonini cheklashi mumkin, shu sabab oldindan aniqlashtirib olish tavsiya etiladi."
            ), order_index=3,
        ),
        FAQ(
            question="Ihromda nimalar taqiqlanadi?", tag="Ihrom",
            answer=(
                "Ihromdagi kishiga hid sepish, soch-tirnoq olish, ov qilish, nikoh o'qish, jinsiy "
                "aloqaga oid gap-so'zlar va janjal-nizo kabi amallar taqiqlanadi. Erkaklar uchun "
                "qo'shimcha ravishda tikilgan kiyim kiyish ham man etiladi."
            ), order_index=4,
        ),
        FAQ(
            question="Ayollar ihromda alohida kiyim kiyishlari kerakmi?", tag="Ihrom",
            answer=(
                "Yo'q, ayollar uchun maxsus ihrom kiyimi shart emas — ular odatdagi hashamatsiz, "
                "vujudni yaxshi yopadigan kiyimlarida qolaveradi. Faqat yuzni butunlay yopuvchi "
                "niqob va qo'lqop kiyish odatda man etiladi."
            ), order_index=5,
        ),
        FAQ(
            question="Ihrom buzilsa nima qilish kerak?", tag="Ihrom",
            answer=(
                "Ihrom paytida taqiqlangan biror amal beixtiyor sodir bo'lib qolsa, holatga qarab "
                "fidya (kompensatsiya) to'lash lozim bo'lishi mumkin. Bunday holatlarda mahalliy "
                "bilimdon ulamodan maslahat olish eng to'g'ri yo'ldir."
            ), order_index=6,
        ),
        FAQ(
            question="Umra safariga qancha vaqt oldin tayyorgarlik ko'rish kerak?", tag="Tashkiliy",
            answer=(
                "Odatda vizani rasmiylashtirish, chipta va turar joy band qilish uchun kamida "
                "bir-ikki oy oldin tayyorgarlikni boshlash tavsiya etiladi, ayniqsa Ramazon yoki "
                "Haj mavsumiga to'g'ri kelsa, bandlik ancha oldin to'lib qolishi mumkin."
            ), order_index=7,
        ),
        FAQ(
            question="Umra safarida sog'liqni saqlash bo'yicha nimalarga e'tibor berish kerak?", tag="Sog'liq",
            answer=(
                "Issiq iqlim va katta izdihom sabab ko'p suv ichish, qulay va yengil poyabzal kiyish, "
                "quyoshdan himoyalanish hamda safar oldidan zarur emlanishlar (tavsiya etilgan "
                "vaksinalar) haqida shifokor bilan maslahatlashish foydali bo'ladi."
            ), order_index=8,
        ),
    ]
    db.add_all(faqs)

    db.commit()
    db.close()
    print("Ma'lumotlar bazasi muvaffaqiyatli to'ldirildi ✅")


if __name__ == "__main__":
    seed()
