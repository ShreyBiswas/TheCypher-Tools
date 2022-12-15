from splitters import splitIntoChunks, splitInto

text = "IHRHGFTVEEEENNPOAIAOLARAEIEETINNBKLSPREEETNRMRAHSENEUNIIUMNDDTANWREAMOAYDMCDJNERETSNADAANFBYOAYMIDOILJKRBGWHIUANFTGBRESVMTFTAOAEEOOSERYOEEASANDTETVODIOERSMSNNLCSHEENNURYALIAWNWPUDSUANNNEECMRCENANROITPLETBRRUYGHSTNENLOLGIOUEEGIASTFOLEEYRSMKIITTITDHCFSINSOUCEIISEANOTEREMESINGIIANEACVWENMEIDRAEOTRDSRONRCOTTTTATGCUOLBEMESTDRFAIRIEAANMTDUROIELDDLEENFCUPAEWHTTLHNGCNRSNATDRANTELIICNFDEEOREIVVEESONIEHFSNHNATLREAWUOOSTATRISOSAOTSDSSASRISIIEARONDESTRUOWEAESNLHTMENEIGKDDSTBELDUIPTNWAELMSDERTIOYEMGHWLODPUULVSTTDEMLGPCEODHPITREAHFRHSYABTUNDOECOEEPRSSTDWIENMNMOIDFRMEINHYECSSUDNMUNDSOSTAUCMDENRADVTTAROTSNLAISNISKUENCAEPELGATSDEEAIRDSHBITOEGPBODEEFDISRODNISTTSUEUCTSACGWDROENOONIRWDENNTODICINOMNLLOSSEOTFREOLMACSOOPSDOHDFIRGKTNECIROEROOHWBCCPNOARDITNBKCAENOBIEUDTYEYOOFIGAMUDHGRCBONEORHHIREHEEROINSDRNUTETIAAIXUASOIEIEIDTRTENNZMCTOLECSCIDNENCNPVOTTDOEGEOOOHDDRNFWUHENNAIURTSEDDDSSIYSRHHELNEOSOUSNELVTMDGNWDTDAAMELXANEFEIENRECTOUNSKKODTASHNGGEEIOTEELEUENRISOROANGALNTFCDRVUINMDDAUHNLNMIVADFNEBGOARRITEEOAERENNREIREDERDIEDRULDBITISYATENEOLFDSHERNRETBEIILOTOBDTOWRIRNSDANHEEAUEETNSTNMREMTSMEOTLESTUHEIIIAIATPGMEHTEAABMENTCNEATEBNIDERGNTIDCRFNWCRHRNRDPREOORRATOOUSARCNBGTHHMLTETPIAEEICFEFNLDTOPNNAINIHTAATTNTIDIOEETNREEMRHEHABHGTTSENUOEIESTDEIOSINHCTSTBNNDRCANENHNAWTNIYTHAITASPSSCOEAOHATHBDOTBRDTMECINWEGEGHEREERNBOLHEKANSNDFASRXIYEOAGLTNESEMIAIIYNGAXURETLATEUGENTPHNCCLSEHTIDRLIAEPIBEAIYOOCVNIWRTLYEOAFITBHWOOLTATMPOFSGFLWIODNFVTATEDADREUETHCOEWAMWNENGNREWPIAATDEPOSIETEWMAHESRRAEHIASTFHATNNERDTCSEUMNSDNETOTTNEWRITMLDEHGDMEHEABHSWSSOASRTDTHDYDEGEOHOEFNIGIAHEIYMEATUOESTERXUACEDVHTTAHNNOFSRTLNBUIERTIAEEDMWTPCRREDEELHETHIEEEUUEISLIRITMCHYEHLVBTOTVAAFOBDAOPMWLNODTLTSNHWOATIBEEDXOTTTEIRTHSPMOONGNEPHBOSOUOLFNHAGDTESIGLTNETTEATTRDMOLYVSMESEAGENSNEEOFNTOWTFPRSRWNRIRFAEGHEFLISOUIOTRAYTNHIHSPEESFLIEDIGRSEEAIYARESAHNNPIGESTTAXOSEIIYGAENGPETDNGEFEHOTEARPCWENNONTBRDERVLOEOTNOIGMRNEEOHRESSOSDUDRLOFATLEEECIHNTETBDHUCRHBAOEASITWTNSSNMHOOLLAONIGOHCETSOSECDRIONIHXAEMSAROSRUNRCAOHHOIVAIAATNISVTHSNOHOSWUETYISEREYOHNTEERLRNIMSLEHGTNTEEOROSTOCENENAFELEBHDTOWHEIDOSERTTSAOXTUIERSTFSTINPWIDIEEELWCWAIFHCCOAHLOHCVPNERXOHHACEEIEEECEAOANWTMMTCODNHDEEDBFENASCEAOSBTMKLNSGOHCNBPUDRKYOEYSEDETTSRENFHHEHETSOSUWUADEESTAOOEYTBAHLXWSYNIMLEFATETIAOSRPAIEATNNISROHSHMNBNAGROEBTOSENEHHESELDOMBOSSFTUEDUEHAESTUOAXGTSDITSETPTDBWDFRTAIYRTREETIERESNDHOALSTOCIETRNHTEDCPMEOESTHOOAEEARDAERUYNSNHHESREEFOOLAOTTNTTSIOWRILOSETNEIAERTPNFHYOPEBRNRANOIRNAMODHUTMTESNSTHUBKPOMNEICITSCREVAEFIKQBHCEICCENHTASTERSUAOSOOIAGFFNSTPOEEEIIEPENOSRMHTTOEMRAADATUNISEOUSMMALNKBSBTEFCEUFNRDUNYASOTESCERGOBOTYGNDHUNHEAITEUEEARTNIOUYPEORWUNTNEIEAOCGRTCRRAMNNTSCIUQSHTIIAGTNHREEIESKAUDAAXTSHUTEHAHERESOEIECOVTBOSGDIJTNNNTOUMSEALUIAFAODFNAEINDAFTYTATENKGWRNOAETRYESOSTNDATWNRSNRUNESEOEISNEEOITMRMNWTTOIAOTTRNNWATNWTYWSYTIINORDAAOOHAEHESINWJGTRHSNVNRTTEEONGOCEHKEEFRRISKHESEOGKHIRSIFPAGDNIFOADOEAREWKGHTITOWREEAERCORUWFUTOHEUECFTNCRENOTOEOITGACETRAOYOICEIUTNEESITDIODHEOENLSHOEISUSBDTNARUOTENERSDEARSTDTADEEPEWTIUDANITPRIPHNIOENOETEPTRVGAGRMRNUHUIRRVSEISGCLICMAUSSTIOOMANTEAEOYSDFRREEDNTDSREOANSAYFGFRIMCTOLOAFMYITEMRIUTLSPTBEGFNNPNTSAUAOKGTYAVEIOMNYTRNOEMHIGSSKANPHFCRNRTATOOEATPEDOUHTNOEWTBELDSEDIDDEBOCBEEPTIOVEAEATSRSEEEIDLPIWRSPUHBADVEHTNNFLROENTOAIHUSEHNWEFFGDLTTOSEETEUDDHEVREEUNFUETAAWHAEOVTMCARRHITSWLHONHEU"

text = splitIntoChunks(text, 125)

text = [splitInto(text[i], 5) for i in range(len(text))]

[print(i) for i in text]


def getFirstBlock(text):
    # get all the first items
    return [i[0] for i in text]


t = getFirstBlock(text)
print("\n".join(t))


def rotateRow(text, row, amount=1):
    # rotate the column
    return [text[i][row:] + text[i][:row] for i in range(len(text))]


def rowsToColumns(text: list[list]):
    # convert a list of rows to a list of columns
    return [
        "".join([text[i][j] for i in range(len(text))]) for j in range(len(text[0]))
    ]


def columnsToRows(text: list[list]):
    # convert a list of columns to a list of rows
    return rowsToColumns(text)


def rotateRow(text, row, amount=1):
    # rotate the row
    text[row] = text[row][amount:] + text[row][:amount]
    return text


def rotateRows(text, amount=1):
    # rotate the rows
    return [text[i][amount:] + text[i][:amount] for i in range(len(text))]


def rotateColumn(text, col, amount=1):
    text = rowsToColumns(text)
    text = rotateRow(text, col, amount)
    return columnsToRows(text)


def rotateColumns(text, amount=1):
    text = rowsToColumns(text)
    text = rotateRows(text, amount)
    return columnsToRows(text)


# t = rotateColumn(t, 22, 6)  # U
# t = rotateColumn(t, 23, 5)  # D
# t = rotateColumn(t, 19, 4)  # P
# t = rotateColumns(t, 4)
print("---")
print("\n".join([" ".join(x) for x in t]))

letters = "under"
print("---")
for i in t:
    # print i if all of the letters in letters are in i, though not in order
    if all([x in i for x in letters]):
        print(i)

# see if rotating the last few columns will create the word 'underthe'