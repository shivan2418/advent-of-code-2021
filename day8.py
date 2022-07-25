import math
import re
from typing import List

import tqdm

test_input = '''
2199943210
3987894921
9856789892
8767896789
9899965678'''

input = '''
0198954334976942239109321545998999878998764656978999349899965478954987432389012356989932123998432123
1997943129865890198998910239867899967999873249865988998799896567899876543478925689879899019896421012
9886895997654789987987891998756898656987654598774877897545697878912988654567934598767688998789432123
8765789869763567996545789876545999768998798797653656796536789989543499867688955697654567897678954235
9876898753212456989434679987976789879239899898542348987421568997699989878999896898753656797569765376
0987899854901345678923478998987999989998975959643459876542456789988978989998789999842349899678997487
2398959769892957789012467899898999899897654345987678987543567999876767897987678898761018999789998598
3599549898769898993123458987639998789789532123498989898654698999965459975698545789983567899899987679
4989432999656799654364667996521989598678944234989796789765789798754368964679657899894589989999898791
9879949897545678967975878989432978436567954349876535699977997679854234943569869998765999879989769890
9867898765434589878989999578999767323457895456995323798989543569542123899699878909879876768678953989
8757989987645678989092123489987656212345889679899213997999432198654235678989989212998875654569769979
7645678998656789299297334569876543101345678998778939876898954569764345989678994323497964323468998767
1534578999767899198986586679987764512387989876567898765457895678985469994569765434596543212356789156
0123467899898978987897898899998975643478995965479986543234999789876598989678998645987632103568993245
4235678979979569876789919968999997856569654987567895432155679896987897878989679876898545314789754766
5546789765765459984568923459987898768679653498689976621019989954398986567893498989987695424898769889
7856797654432397213467894698876569878789432398798986543198895432129875456912987698998986546789878996
9768899843101976434688999987766456989998953789897897654987789843299764347799654567899797656789989645
9878998754233987549789988996651238898767895678956798969976699754987643235678965678987659878999993234
7999899965654797679895677965430356789456976799347679998764568967999654016889986789876542989569892129
6986789876795698989923456894321246794239897893234578976543487898998765127999999899987821093459789098
5435667987986999999874567896534356789949789921015679895322346789019976238989899999876542912998678997
4323459899897898998965678997647467997898679933234599797401367898923987349976678989987669899876467896
3212998789789987987989789398766567896976568899545988689212456897945698967895457978999798767987679965
4309875646678996556899891249877899954320446798959876578999567976899789879964349865789899654598989334
3219554234569219434989954398988921967431234567898765467678978965789893989998599974899999543499793212
4997432123678998999879765987699999876546346788999985336589989994896902498987678989989998932987654329
9876543245989987889968999876543989987687897899999896213467999876895213567898789299765987821298775678
8987854556894345678956789998679876999798998999889798101578910987894394678939891019873496532999896799
7698976677954234599745699998798884899899329998765689313489421598965989899423932198921987649899989890
6549987988943123689656789899987653668993210987654569986578932349896978989214949997532398999768878921
7756798999431012698769998789776542557989421297643467899789543456799869878929898889543459987653567992
8987899998999243459898789698654421345678932398654578979899956789987659767898787678999767998542456789
9898968997988954568965698598793210156899645469767699467989897899897745656989654589988978987631375699
8769656986567897679654596439987921367998756899878789359878789998765432345679543598767899997410134789
9954249987456898989768987521986434456789867987989992198767678999876521349889901987543339876321245679
9865198765345689199979765430987545768999998946797893987654597898765435478999893976432129865434357889
9991029984296891019999876542398969899998999235986789976543656799876556569998769896554239876545667998
8789129876989932998945989653989898989987898949875696989652345789987987678987657789665445987676878957
8688999999878949877896798799765787679896767898754245799921235689298998789876546678989589998989989545
7567989987857899765679979987654567589765456789876126999832367893109459899997434568997678999898998734
5499879765436987654569865598743423469876877896521099898753456954212345999998528678998789987787899949
6987656976524599543678954329832102378989988965433987659864869896793469998999838989899899876576999898
9998767897434598956789765497643236899993499977654976540975998789954598987898646898765998765445899656
8999879976545987997899876987654345678901943988779765321986989697899987876789757999954239654325678945
7786989997659576889978998998785459789219892399889898732399878545678976745699768998932199867214589656
6565799989897465679567899999897878994329789902999987543498767435699765434567978987893987654323578997
5444679878986323493456789988998999789998678893498998684569854324589854315779989876789998875634699398
6323498759875437894667899976549446699876558789976439795698765416678952104567899865698999987849893249
3212989643986556789988999895432234579987345679765429898789876527899543212388998764587992198967910123
5459876532398767993299998794320123992392136789975212969899998678987656623499987653376789349978921235
6597954321239878932134987689321399889989015699894353459999598789798787536567899762165567999989932446
7986543210157989321029876578932988779678923456789877678998439896689876547679959854013456789299873457
9797676521238996432134965489549976567567894578897998989987510975468989658789749862134567892198765678
4598997432347896543549876379698765456456789679986549999899329876349898778895539879345679943999986899
3569986543456789656867976568999866331345678989995434987679949983299769899984320987656997899892197975
2345698754578999767979498689987653210234899998976219876569898654987653969865421498767896798789998944
1236999885679789998989239795498769329946789877894398765498789769765432358977432389878975434569899432
0349899976789678999894349892349898998897898966965987654397689879877841237898743467999664313467789901
1239798999894589998765956901467997987789956645899899765298797989998930356789654569876543201234569892
2998667899923458929879899892568985465678943234789678953129896595699321268898789678987654562365698789
9876545798912347912998789789879875323489432123596567891012999434987532379999898799498765684578987678
9988432977893456894989645678998763218796543034789437789234678929876543456789959989329876795789876567
9895431866789579999876534569899953105689656546797645678945799101987854579899349878912989897899865456
8765310145689998999998321345798767214578998687899856789996893212398965699998969769653499998912976367
7654321234567896789874210127789874323789998788967967892987894323569879789987898758994689579201985458
8765432365679944598765331235699985434899999899459878921998995437689989891976789347889793459399876769
9878944456989533459876452346789996546789896912345989439899986568789299932987894236778965998988987878
0999876567895421246986567487997897657899774101236799598788997679892109893498956124568999876267898989
1989998698996730178987878998976798768987653212345678987697898793999298789569743013456789994348939996
9878999789987541359998989659365679899987654323657799986576799892398997678998652124567893986789129895
8767899893496432499899997643234899999998765434567899975425678901986554599998543236899964799891098796
7654698921297543987789999832123789998799886865678949876534799999876423678987654545678975678942989689
9543567890987665996578898753435678987689997976789421987646789987654213589998778659899986789659876548
8912478999998789875466789766576789986579999987896610198757891098785344567999899789967997898998998957
7894567898999896984345678987687898765459892199965423459868989129887895678999929892158998987897899868
6789789987899934986456789298998949654328789013986594569879578934999976899889012999349989675876789979
4899998756789915698567899129989939869212578923987989978989459899653987897678929998959876543365679989
5999897647897896987678988999867899998923459994699677899392398798942398928568998997899985432124567890
6898765530146789999789567989654678987995767989987566789210987687890999312456987976899899321013479931
7919654321237898989892379878943569895789999878976455899391296566799889202369876345697778934154567899
8929865445356987579954998769892398784679889767895324988989987434789768943459965237986567953245679978
9934986656767893467899877555679989613498767856991015976568986523598546899698954356975468967456789767
9899997768978922279923965434568976501987845345689129896459876434987656998987895479864357978697997656
8767898989989210189109874323457898319876431234568999765345987845699767897796989599865267899789996545
7656899591095332398998765446568987634986545489679988653236798956789878986675978987654356789899989326
8767999432986745567899976757678976545697657567989876542124569979892989965434567898865468993999878939
9898998993987857898967987878789989656789967979399986321013456989901399876512367899979878921298769998
2999987789998969999458998989896799778999878989298765442134567895313567985403456897989989942987657897
1298986678999878998569769997955459889901989892129876653485698989494579875314567896998796899996545956
0987854567999999987678956976545368999892398763012989764578789876989989994323698965789545678989434345
9876783456889323498789543989631259999789987653135699876689992345678999985554789654678924579879921267
9965432345679212589896532398920345987678998774256789987799101256799339876765896532467896798768895348
9876543456798954679987421987934599793589998765345678998898942349989212989876897651278999986545789458
3998654567897799798899910986899987654678939978458799769987895498968999995989965432345698765435679567
2198777679976687987678891965678999769899212989569897654216789987654678954399877643567899654323569678
1019888789465456986546779878999239878989103498678998765345678999543789967894998654689998795434578989
2123999994312349876534567989654347989378915679789329876557789987654567898923498765891019986795989295
3235986543201456987677678999987656896567923899893212998768994399765678999434569978943523987886892123'''


class Point:
    row_length = None

    def __str__(self):
        return f"{self.height}"

    def __repr__(self):
        return self.__str__()

    def __init__(self, up, down, left, right, height, uuid):
        self.up = up
        self.down = down
        self.left = left
        self.right = right

        self.uuid = uuid

        self.height = int(height)

    def all_adjacent_are_higher(self):
        nearby_heights = []
        nearby_heights += [int(self.up)] if self.up else []
        nearby_heights += [int(self.down)] if self.down else []

        nearby_heights += [int(self.left)] if self.left else []
        nearby_heights += [int(self.right)] if self.right else []

        return all([h > self.height for h in nearby_heights])

    def add_links(self, points: List['Point']):
        self.up_link = points[self.uuid - Point.row_length] if self.up else None
        self.down_link = points[self.uuid + Point.row_length] if self.down else None
        self.left_link = points[self.uuid - 1] if self.left else None
        self.right_link = points[self.uuid + 1] if self.right else None

    def get_all_adjacent_links(self):
        return [link for link in [self.up_link, self.down_link, self.left_link, self.right_link] if link is not None]

    def has_unmapped_adjacent_tiles(self, already_mapped_tiles):
        return len([link for link in [self.up_link, self.down_link, self.left_link, self.right_link] if
                    link is not None and link.height != 9 and link.uuid not in already_mapped_tiles]) > 0

    def valid_adjacent_tiles(self, already_mapped_tiles=None):
        if already_mapped_tiles is None:
            already_mapped_tiles = []
        valid_adjacent = [link for link in [self.up_link, self.down_link, self.left_link, self.right_link] if
                          link is not None and link.height != 9 and link not in already_mapped_tiles]
        return valid_adjacent


def create_points(input):
    q = [l for l in input.split('\n') if l != ""]
    row_length = len(q[0])
    Point.row_length = row_length
    points = []
    formatted_input = re.sub(pattern=r"\D", string=input, repl="")

    for n, char in enumerate(formatted_input):
        try:
            left = formatted_input[n - 1] if n % Point.row_length != 0 else None
        except:
            left = None
        try:
            right = formatted_input[n + 1]
            if n % Point.row_length-1 == 0 and n != 0:
                right = None
        except:
            right = None
        try:
            up = formatted_input[n - Point.row_length] if n - Point.row_length >= 0 else None
        except:
            up = None
        try:
            down = formatted_input[n + Point.row_length]
        except:
            down = None

        points.append(Point(up, down, left, right, char, n))

    for p in points:
        p.add_links(points)

    return points


def get_lowest_points(input):
    points = create_points(input)
    lowest_points = sum([p.height + 1 for p in points if p.all_adjacent_are_higher()])

    print(lowest_points)


def map_tiles(starting_tile: Point):
    mapped_tiles = [starting_tile]
    tiles_to_map = starting_tile.valid_adjacent_tiles([])

    while len(tiles_to_map) > 0:
        new_tile = tiles_to_map.pop()
        mapped_tiles.append(new_tile)
        tiles_to_map.extend(new_tile.valid_adjacent_tiles(mapped_tiles))

    assert len([p for p in mapped_tiles if p.height == 9]) == 0

    return len(set(mapped_tiles))


def find_basins(input):
    points = create_points(input)

    lowest_points = [p for p in points if p.all_adjacent_are_higher()]

    basin_sizes = []

    with tqdm.tqdm(total=len(lowest_points)) as bar:
        for lowpoint in lowest_points:
            basin_sizes.append(map_tiles(lowpoint))
            bar.update()

    basin_sizes.sort()
    print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])


if __name__ == '__main__':
    get_lowest_points(test_input)
    get_lowest_points(input)
    find_basins(test_input)
    find_basins(input)
