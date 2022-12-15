def display(rows):
    for row in rows:
        print("".join(list(row.upper())))


def displayMultiple(rows):
    """Display multiple chunks side by side."""
    for row in zip(*rows):
        print(" ".join(list(row[0].upper())), "  |  ", " ".join(list(row[1].upper())))


def shiftLeft(rows):
    """Shifts the rows up by one position."""
    return [rows[i][1:] + rows[i][0] for i in range(len(rows))]


def shiftUp(rows):
    """Shifts the rows up by one position."""
    return rows[1:] + [rows[0]]


def shiftRight(rows):
    """Shifts the rows right by one position."""
    return [rows[i][-1] + rows[i][:-1] for i in range(len(rows))]


def shiftDown(rows):
    """Shifts the rows down by one position."""
    return [rows[-1]] + rows[:-1]


def rearrangeRows(text, order):
    """Rearranges the rows of text according to the given order.
    Returns a list of strings.
    """
    if len(order) != len(text):
        print(order)
        raise ValueError(
            f"Different number of rows ({len(text)}) and order elements ({len(order)})."
        )
    return [text[i - 1] for i in order]


def rearrangeRowsMultiple(text: list[list], order):
    """Rearranges the rows of text according to the given order.
    Returns a list of strings.
    """
    for textChunk in text:
        yield rearrangeRows(textChunk, order)


def rearrangeColumns(text, order):
    """Rearranges the columns of text according to the given order.
    Returns a list of strings.
    """
    if len(order) != len(text[0]):
        raise ValueError(
            f"Different number of columns ({len(text[0])}) and order elements ({len(order)})."
        )
    for i in range(len(text)):
        text[i] = "".join([text[i][j - 1] for j in order])
    return text


def rotateColumns(text, numRotations):
    """Rotates the columns of text by the given number of positions.
    Returns a list of strings.
    """
    for i in range(len(text)):
        text[i] = text[i][numRotations:] + text[i][:numRotations]
    return text


def rearrangeColumnsMultiple(text: list[list], order):
    """Rearranges the columns of text according to the given order.
    Returns a list of strings.
    """
    for textChunk in text:
        yield rearrangeColumns(textChunk, order)


def interface(text):
    display(text)
    while True:
        command = input("Row (r) or column (c)?\n")
        if command == "r":  # row
            text = rearrangeRows(text, [int(i) for i in list(input())])
        elif command == "c":  # column
            text = rearrangeColumns(text, [int(i) for i in list(input())])
        elif command == "rot":
            text = rotateColumns(text, int(input("Number of rotations?\n")))
        elif command == "l":
            text = shiftLeft(text)
        elif command == "u":
            text = shiftUp(text)
        elif command == "r":
            text = shiftRight(text)
        elif command == "d":
            text = shiftDown(text)

        print("------------------")
        display(text)


def interfaceMultiple(text: list):
    displayMultiple(text)
    while True:
        command = input("Row (r) or column (c)?\n")
        if command == "r":  # row
            text = rearrangeRowsMultiple(text, [int(i) for i in list(input())])
        elif command == "c":  # column
            text = rearrangeColumnsMultiple(text, [int(i) for i in list(input())])

        print("------------------")
        displayMultiple(text)


if __name__ == "__main__":
    text = "IHRHGFTVEEEENNPOAIAOLARAEIEETINNBKLSPREEETNRMRAHSENEUNIIUMNDDTANWREAMOAYDMCDJNERETSNADAANFBYOAYMIDOILJKRBGWHIUANFTGBRESVMTFTAOAEEOOSERYOEEASANDTETVODIOERSMSNNLCSHEENNURYALIAWNWPUDSUANNNEECMRCENANROITPLETBRRUYGHSTNENLOLGIOUEEGIASTFOLEEYRSMKIITTITDHCFSINSOUCEIISEANOTEREMESINGIIANEACVWENMEIDRAEOTRDSRONRCOTTTTATGCUOLBEMESTDRFAIRIEAANMTDUROIELDDLEENFCUPAEWHTTLHNGCNRSNATDRANTELIICNFDEEOREIVVEESONIEHFSNHNATLREAWUOOSTATRISOSAOTSDSSASRISIIEARONDESTRUOWEAESNLHTMENEIGKDDSTBELDUIPTNWAELMSDERTIOYEMGHWLODPUULVSTTDEMLGPCEODHPITREAHFRHSYABTUNDOECOEEPRSSTDWIENMNMOIDFRMEINHYECSSUDNMUNDSOSTAUCMDENRADVTTAROTSNLAISNISKUENCAEPELGATSDEEAIRDSHBITOEGPBODEEFDISRODNISTTSUEUCTSACGWDROENOONIRWDENNTODICINOMNLLOSSEOTFREOLMACSOOPSDOHDFIRGKTNECIROEROOHWBCCPNOARDITNBKCAENOBIEUDTYEYOOFIGAMUDHGRCBONEORHHIREHEEROINSDRNUTETIAAIXUASOIEIEIDTRTENNZMCTOLECSCIDNENCNPVOTTDOEGEOOOHDDRNFWUHENNAIURTSEDDDSSIYSRHHELNEOSOUSNELVTMDGNWDTDAAMELXANEFEIENRECTOUNSKKODTASHNGGEEIOTEELEUENRISOROANGALNTFCDRVUINMDDAUHNLNMIVADFNEBGOARRITEEOAERENNREIREDERDIEDRULDBITISYATENEOLFDSHERNRETBEIILOTOBDTOWRIRNSDANHEEAUEETNSTNMREMTSMEOTLESTUHEIIIAIATPGMEHTEAABMENTCNEATEBNIDERGNTIDCRFNWCRHRNRDPREOORRATOOUSARCNBGTHHMLTETPIAEEICFEFNLDTOPNNAINIHTAATTNTIDIOEETNREEMRHEHABHGTTSENUOEIESTDEIOSINHCTSTBNNDRCANENHNAWTNIYTHAITASPSSCOEAOHATHBDOTBRDTMECINWEGEGHEREERNBOLHEKANSNDFASRXIYEOAGLTNESEMIAIIYNGAXURETLATEUGENTPHNCCLSEHTIDRLIAEPIBEAIYOOCVNIWRTLYEOAFITBHWOOLTATMPOFSGFLWIODNFVTATEDADREUETHCOEWAMWNENGNREWPIAATDEPOSIETEWMAHESRRAEHIASTFHATNNERDTCSEUMNSDNETOTTNEWRITMLDEHGDMEHEABHSWSSOASRTDTHDYDEGEOHOEFNIGIAHEIYMEATUOESTERXUACEDVHTTAHNNOFSRTLNBUIERTIAEEDMWTPCRREDEELHETHIEEEUUEISLIRITMCHYEHLVBTOTVAAFOBDAOPMWLNODTLTSNHWOATIBEEDXOTTTEIRTHSPMOONGNEPHBOSOUOLFNHAGDTESIGLTNETTEATTRDMOLYVSMESEAGENSNEEOFNTOWTFPRSRWNRIRFAEGHEFLISOUIOTRAYTNHIHSPEESFLIEDIGRSEEAIYARESAHNNPIGESTTAXOSEIIYGAENGPETDNGEFEHOTEARPCWENNONTBRDERVLOEOTNOIGMRNEEOHRESSOSDUDRLOFATLEEECIHNTETBDHUCRHBAOEASITWTNSSNMHOOLLAONIGOHCETSOSECDRIONIHXAEMSAROSRUNRCAOHHOIVAIAATNISVTHSNOHOSWUETYISEREYOHNTEERLRNIMSLEHGTNTEEOROSTOCENENAFELEBHDTOWHEIDOSERTTSAOXTUIERSTFSTINPWIDIEEELWCWAIFHCCOAHLOHCVPNERXOHHACEEIEEECEAOANWTMMTCODNHDEEDBFENASCEAOSBTMKLNSGOHCNBPUDRKYOEYSEDETTSRENFHHEHETSOSUWUADEESTAOOEYTBAHLXWSYNIMLEFATETIAOSRPAIEATNNISROHSHMNBNAGROEBTOSENEHHESELDOMBOSSFTUEDUEHAESTUOAXGTSDITSETPTDBWDFRTAIYRTREETIERESNDHOALSTOCIETRNHTEDCPMEOESTHOOAEEARDAERUYNSNHHESREEFOOLAOTTNTTSIOWRILOSETNEIAERTPNFHYOPEBRNRANOIRNAMODHUTMTESNSTHUBKPOMNEICITSCREVAEFIKQBHCEICCENHTASTERSUAOSOOIAGFFNSTPOEEEIIEPENOSRMHTTOEMRAADATUNISEOUSMMALNKBSBTEFCEUFNRDUNYASOTESCERGOBOTYGNDHUNHEAITEUEEARTNIOUYPEORWUNTNEIEAOCGRTCRRAMNNTSCIUQSHTIIAGTNHREEIESKAUDAAXTSHUTEHAHERESOEIECOVTBOSGDIJTNNNTOUMSEALUIAFAODFNAEINDAFTYTATENKGWRNOAETRYESOSTNDATWNRSNRUNESEOEISNEEOITMRMNWTTOIAOTTRNNWATNWTYWSYTIINORDAAOOHAEHESINWJGTRHSNVNRTTEEONGOCEHKEEFRRISKHESEOGKHIRSIFPAGDNIFOADOEAREWKGHTITOWREEAERCORUWFUTOHEUECFTNCRENOTOEOITGACETRAOYOICEIUTNEESITDIODHEOENLSHOEISUSBDTNARUOTENERSDEARSTDTADEEPEWTIUDANITPRIPHNIOENOETEPTRVGAGRMRNUHUIRRVSEISGCLICMAUSSTIOOMANTEAEOYSDFRREEDNTDSREOANSAYFGFRIMCTOLOAFMYITEMRIUTLSPTBEGFNNPNTSAUAOKGTYAVEIOMNYTRNOEMHIGSSKANPHFCRNRTATOOEATPEDOUHTNOEWTBELDSEDIDDEBOCBEEPTIOVEAEATSRSEEEIDLPIWRSPUHBADVEHTNNFLROENTOAIHUSEHNWEFFGDLTTOSEETEUDDHEVREEUNFUETAAWHAEOVTMCARRHITSWLHONHEU"
    from splitters import splitEvery, splitIntoChunks, splitInto

    text = splitIntoChunks(text, 25)
    interface(text)
    # interfaceMultiple(splitInto(text, 25))
