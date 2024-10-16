import axios from "axios";
import vCardJS from "vcards-js";

const getBase64FromUrl = async (url) => {
  const { data } = await axios({
    method: "GET",
    url,
    responseType: "blob",
  });

  return new Promise((resolve) => {
    const reader = new FileReader();
    reader.readAsDataURL(data);
    reader.onloadend = () => {
      const base64data = reader.result;
      resolve(base64data);
    };
  });
};

const generateVCF = async () => {
  const base64Img = await getBase64FromUrl(
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2ukppM2XgArR7MtxpPVzUDeXPGA-gcBoSug&usqp=CAU"
  );

  const b64 = base64Img.replace(/^data:image.+;base64,/, "");

  // Add all contacts
  const contacts = [
    { name: "COCAN WORLD", phone: "01028067666" },
    { name: "JELLAVU", phone: "01064112044" },
    { name: "IN YOURSHoE", phone: "01223686410" },
    { name: "FRILLA", phone: "01222125998" },
    { name: "Amira store", phone: "01007863516" },
    { name: "Diva Diana", phone: "01001505519" },
    { name: "Zainab", phone: "01113666375" },
    { name: "MEHOS", phone: "01222877834" },
    { name: "MANOLLI", phone: "01223911543" },
    { name: "MOONLIGHT", phone: "01140027732" },
    { name: "RANIA MATTAR", phone: "0122316700" },
    { name: "TALEED", phone: "01005083320" },
    { name: "NINA SHAWKI COLLECTIONS", phone: "01007119745" },
    { name: "YALA BOUTIQUE", phone: "01063511117" },
    { name: "GERBERA SHAYMAA ALSHAARAWY", phone: "01011161762" },
    { name: "VOUCHER", phone: "01144857777" },
    { name: "NOON ART", phone: "028477184" },
    { name: "THE SELECT", phone: "01287987008" },
    { name: "OYA", phone: "01222174445" },
    { name: "COQUETTE", phone: "01200200819" },
    { name: "NADA GOMAA", phone: "01007669699" },
    { name: "CARPET LAND", phone: "000015406" },
    { name: "DANANEER", phone: "01065828100" },
    { name: "RABAB SHERIF", phone: "01006501494" },
    { name: "THE CAPE", phone: "01116618982" },
    { name: "DODO DESIGNS", phone: "01156444378" },
    { name: "ASH DECORATION", phone: "01096811058" },
    { name: "SILA", phone: "01140702424" },
    { name: "MOUNIRSTEXTILE", phone: "01006767632" },
    { name: "NORAAMIN DESIGNS", phone: "01273774377" },
    { name: "DEL MAISON", phone: "01023422255" },
    { name: "LAMSA MASREYA", phone: "01210040460" },
    { name: "HAND MADE JE WELRY", phone: "0126969235" },
    { name: "مخبوزات بيتي", phone: "01024808703" },
    { name: "GERBERA", phone: "01155633011" },
    { name: "MED CEUTICALS SKIN HAIR LOBS", phone: "01210857771" },
    { name: "MINIMA", phone: "01050777505" },
    { name: "ثياب", phone: "01001524269" },
    { name: "ELLIEHOME", phone: "01024365484" },
    { name: "FUFA", phone: "01149969084" },
    { name: "ECRU", phone: "01014048347" },
    { name: "HBSHOP.CO", phone: "01110357445" },
    { name: "HALA EZZATE", phone: "01003999011" },
    { name: "JOUZOOR", phone: "01013289132" },
    { name: "K&A HOME", phone: "01024448771" },
    { name: "MAHA THARWAT", phone: "01111211174" },
    { name: "NK DESIGNS", phone: "01008098310" },
    { name: "YASHMAK SCARF FOR WOMEN", phone: "0116600665" },
    { name: "MIRMIA", phone: "01045555722" },
    { name: "المطبخ الريفي", phone: "01019120957" },
    { name: "نــــــــوايا", phone: "01203060666" },
    { name: "SHAML AONLINE", phone: "01026570307" },
    { name: "ECHARPISTA", phone: "01020183548" },
    { name: "CUATROCUISINE", phone: "01008787185" },
    { name: "المغفره", phone: "01126424907" },
    { name: "AKLAHWBALAD", phone: "01017052521" },
    { name: "JRWOMANWEAR", phone: "01110204577" },
    { name: "مجوهرات نوفا فاروق", phone: "01095711894" },
    { name: "ONE.ONE", phone: "01008099100" },
    { name: "BUTTERFIY WOMENCLOTHES", phone: "01150020772" },
    { name: "ELWARSHA ART CRAFT", phone: "01012490390" },
    { name: "NARYA BY CEHAD HABIB", phone: "01090744976" },
    { name: "خمس خمسات", phone: "01129102030" },
    { name: "MIRA S HOME", phone: "01001814593" },
    { name: "FOR WOMEN", phone: "01023270415" },
    { name: "TREND YART", phone: "01202119660" },
    { name: "ALL SEASONS", phone: "01221102979" },
    { name: "BASMA OMER", phone: "01067233000" },
    { name: "EGY ANTIQUE", phone: "01220851567" },
    { name: "NOUR ELDEIN", phone: "01128227089" },
    { name: "الزهروان", phone: "01097755863" },
    { name: "ROLA 1988", phone: "01143737191" },
    { name: "الساحر السوري للموبايل", phone: "01019255658" },
    { name: "JOLO CATERING AND EVENTS", phone: "01080498098" },
    { name: "MAROLRTA HAND MADE", phone: "01154700112" },
    { name: "ELHOSARY", phone: "01050043600" },
    { name: "SADU DESIGNS", phone: "01009458658" },
    { name: "ALEJON", phone: "01070910200" },
    { name: "عالموضه", phone: "01203433774" },
    { name: "M&S", phone: "01126001082" },
    { name: "اسطوره الخليج", phone: "01011037415" },
    { name: "THE FIKKYS", phone: "01002850397" },
    { name: "DELTA STATIONERY", phone: "01282227373" },
    { name: "LABEL", phone: "01115572721" },
    { name: "MARUSKA BOUTIQUE", phone: "01004979150" },
  ];

  contacts.forEach((contact) => {
    const newVCard = vCardJS();
    newVCard.firstName = contact.name;
    newVCard.cellPhone = contact.phone;
    newVCard.photo.embedFromString(b64, "JPEG");

    const cardTXT = newVCard.getFormattedString();
    const file = new Blob([cardTXT], {
      type: "text/plain;charset=utf-8",
    });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(file);
    a.download = `${contact.name}.vcf`;
    a.click();
  });

  btn.style.backgroundColor = "white";
};

const btn = document.getElementById("btn");

