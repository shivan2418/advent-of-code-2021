import statistics
from typing import List

test_input = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''

input = '''([(<<<{({([{{{{}[]}<[]<>>}<{()()}{{}()}>}{((()()))([[]<>]<{}()>)}]({((<>{})[<>()])<{()<>}<<>(
{<{{<[[[(<<<([{}{}](()()))(([][])<()<>>)>>({([[]]<{}<>>)[{[]{}}{[]()}]}[(([]{})){([]<>)}])>((({{<>[]}
[[{<<[{{<[(<[<()<>}[{}[]]]((()()))>{[([]<>)([]())]<([])[{}[]]>})<<<[{}[]]((){})>(<<>[]>[[]<>])>
({[{[<([{((((<{}()><<>()>))[<{[]<>}<{}()>>({<>[]}(<><>>)])([[<()<>>({}<>)]({[]()}[[]{}])]))}
(<<({{{{({[[(<{}{}>{{}<>}){<<>>}]<(<{}()>{(){}}){[{}()]([]<>}}>][([((){})<[]<>>]<<<>{}>{[]}>)(
{(((([{([<[[<[(){}]<()()>>{[[]{}]{{}[]}}]([<<><>>{[]{}}]<{[]()}[()()]>)]((({[]}[<><>]))<<[{}[]][<>()]>([{}[]
([({[[<{[{{[{<{}{}>[<>[]]}(([]()){<><>})]{<<<>()>(()())>{{<>[]}[<>{}]}}}(([(<><>){[][]}][{[]}[[][]]])<([{
<[<{[(([<[([<<()()>{{}{}}>[[<>][{}()]]]({(<>{})}<(<>{}){<><>}>))(<{[{}<>][()()]}<([]())<<>[]>>>)]><
<[([<<{{[(((<[(){}}{(){}}>{[()[]]<[]{}>}))){[[[[<>()](<>())]]]}]{<{(<<{}[]>[<>]><[[]()]<{}[]>>)({[()<>]
(({[<([<<([{{{()[]}{[]{}}}{{<>[]}{()[]}}}<<(()){<>[]}>[(<><>]{(){}}]>]([[({}{})((){})][[<><>]((){})]][{(
{{((<<<{[({[{{()<>}{[][]}}](<([][])[{}{}]>[{(){}}<[]{}>])}<[{{{}{}}(()<>)}[(()<>)[<><>]]]>)(<<[[[][]][{}<>
[({[[{[{[{<((([])){<{}()>{[]{}}})>{<[{()<>>({})][{(){}}<()[]>]>{[{<>{}}(<>{})][<()[]><<>()>]}}
<<{[(<<{{{(<{{[]()}<<>[]>}>{<<{}{}>{[]{}}><[{}{}]{{}[]}>})}{<{[<{}{}>({}())]}{[([]())[[]<>]]<{<><>}
((<[[[([{(({({()()}[{}()])(<{}()>[[][]])}((<[]{}>(<>()))([<><>][<>{}]]))<{([[]{}][[][]])}>
<[<<<<{(((<{[{(){}}{<>()}]}{{{{}()}}<<<>()>>}>{({{<>()}}{<[]<>>[()()]}]}){<(<({}<>){[]<>}>({{}()}(<>())))>
(([[[{{{{<<{<[[]()]{()[]}><[<>[]]({}<>)>}<<{[]{}}<<>>><[{}[]](<><>)>>>[({<{}[]>[(){}]}[{(){}
{[{[({{({<<([({}[])][{()<>}{<>()}])<{<[]()>{()<>}}>>[(<<[]{}>{()()}>)]>})<{[{({<<>[]>{{}()}
<([{[[<[([<(<<<>()><[][]>>)[[[<>()]<<>{}>]]>{<(<{}<>><[]()>)<(<>)[[][]]>>}])]{[[((<({}())[[]{}]><<{}
[([[([{[<({(<({}{})[<><>]>){{({}{})(()())}[([]<>)<[][]>]}}}[[([[[][]]]<({}{})(<>[])>)(([[]()]{<><>})[[[]()
{[[<[<(({<[{<[()[]>{<><>}>([[]<>]{[][]})}([{<><>}<<>{}>][{(){}}[{}<>]])][<(<()<>>(<>()))[{()<>}
(<<<<({[{<[[({()<>}(()()))][({()}[<><>])]]<<[(<>[]){{}()}][([]{})({}{})]>{<[[]<>]<<>()>><[{}()][<>
[({<<{{(<{<<{<()()>(()<>)}<{<><>}>>(([()<>][()<>])[(()<>)(()<>)])>[<(<()<>>{{}()}){[[]{}]{<>{}}}>]}[(<[({}(
({([([[{{[{{{<<><>>{()()}}[[<>[]][()()]]}({{<><>}{<>()}}<({}())>)}<[{[{}()](<>[])}(<(){}>)]
(<{[[[{((<([[<[]{}>([]<>)]{{()()}}]({[{}[]](()<>)}{{{}}[<>()]}))>))}([{(([(<{}[]>[<>()])]({<
([{{<([<{{<[{(()]([][])}][{([])<{}{}>}<([]<>)<{}[]>>]>{<[[[]{}]<{}[]>]<{()}({}<>)>>}}}{<{<<[(){}](()())
{{<<<[{<([<<([{}[]])([()()][()<>>)><({[]()}[()<>])>>]<{[([{}{}]({}[]))]{(({}{}))(<<>()>({}[]))}}{{[[{}{}]<[]<
{[([({[[<{{[{[[][]][<>()]}<<[]()>>]{<{[][]}(<>{})>}}{<[[<><>](<>())](<(){}>({}<>))>[<<[]{}><[]()>>[{[]{}
[{{{([{([[[<{{{}()}{<>[]}}[{<>{}}[[]<>]]>]<([{{}{}]<[]()>]){{{{}()}[<>[]]}(<{}[]>{[]<>})}>][{{[<<>{}><()[]>]
[<[(<(<([(({({{}<>})[{{}<>}{{}[]}]}{[<[]<>><{}[]>][[{}<>)<()<>>]}){{<<(){}>[{}()]><<()>([]<>)>}})
<(([<(([([{([({})][<{}[]><[]()>]){{{[]{}}[[]<>]}<(<>())[{}()]>}}])](<[({(({})(<>()))}{{<[]>}{<<>{}>[()()]
[<{[[{([<{[<(({}{})(<>()))><{{{}<>}<()()>}(<<>()>(<><>))>][[[[()<>]<[]{}>]]{({{}[]}<()<>>)}]}([<<[()()]
([<{{(<(([<{<(<>{})<<>[]>><{{}[]}<[]{}}>}{(((){}){<>()})[<(){}>{<><>}]}>{<([[]()](()<>)){<()>[<><
<(<([({<(([[[[<><>]([]{})]({[]()})](({[]}({}[]))[({}<>)(()())])]<{({[]{}}([]())){<()<>>({}<>)}}
[<(<{(<<<([{<[()<>][<>{}]>{[<>{}][()<>]}}{{<<>{}>[<>{}]}[{(){}}[[][]]]}][{[<[]()>(<>())][<<>[]
[<[[([[[([([[[<><>]({}())][[<>()]]](([[]]({}))[{()[]}({}<>)]))(([{()[]}{{}}][{()[]}[<>[]]])({{<>{}}{
[<[([<<{{{[[[({}{})<()[]>]]]<(({(){}}{(){}})<[{}[]][[][]]>)>}({{([[]{}][[][]])<[<>[]][(){}]>}<[
<[<[({{<(<<[{{<>[]}}[(()())<[]<>>]][{{{}<>}<<>[]]}]>>)<{<(((<>[]))[([])]){(<[]()>({}()))[{{}<
({([<<<<[<{(((<>[])<()()>))<<[<>[]][<>[]]][{[][]}]>}((([[][]])({{}[]}[<><>]))({[[]<>](<>[])
{(<{((({[{({<<()[]>(<>())>{<{}{}><<><>>}}(([[]<>][()[]]){[{}()]}))[<<<<>()}[{}[]]>(<{}{}>{<>[]
(<<[{[([<[<[{(<>{})[{}[]]}([<>[]]<{}[]>)]>](({<{(){}}{{}{}}>}<<{[][]}<{}()>>[{[]{}}{[][]}]>}[{<([]()){<>
{[{{<[[([<{[{([][]){<><>}}[[{}}<<>()>]](<[<><>]({}<>)>[<{}<>><{}{}>])}[<<{()[]}><{{}<>}<<><>>>>([[[]{}]<()<>>
{[<{{([[[[{({{()<>}(<>[])})}(((<{}[]>))<[(()[])[{}{}]><<{}()><(){}>>>)][<(<(()[])((){})><[{}()]<[]<>>>
{<{[[{<[(({[{<()()><{}<>>}{[[]{}]([]<>)}]([({}[])<[][]>]<[[]{}][()()]>)})<(((<<>{}>[<>()])(
[[<{{{(<[{{[[({}<>)<()<>>]]>}{(<[{<>()}]<{{}()}<<>[]>>>{{(<><>){()<>}}[{(){}}<<>{}>]})[{<<()<>>
{[{(<({[[{[{{<[]{}>{[]()}}([[][]][{}{}])}[<{<>{}}<[]<>>>({()()}{[]()})]]<(<{()()}([][])>[{<>
[[{[[<{{({(<{([]()){()<>}}([()()]{<>})>[[{<>{}}({}<>)][{{}{}}<()[]>]])<<[<[]{}>[{}[]]]{[{}[
({({<<{<([[<({[]()}[<>{}]){[{}()][{}<>]}>][<<<{}[]>[{}<>]><<<>>[()()]>><([[]{}]<<>()>>({[]<>}<{}[]>)>]])
{<[{[[{<<([({{<>{}}[{}{}]}(({}{})(<>())))<[([]{}){{}()}]>]([[<[][]>]{<{}[]>{{}()}}]{{[()[]
{[([[[({([<<(<<><>>[[][]])>([<{}[]>])>({{{<>{}}{{}{}}}{<<>{}>({})}}{[{()<>}]})])>([<[{{([]{}){()()}}[{{
<{<(<<{[<([(<<[][]><<>[]>>(<[]{}>(<>[])))])[({(((){}){[]{}})({()()}<{}>)}<<([]())<()<>>>[{<><
<[([{{<<[{([[{<>[]}([][])]]([(<><>){{}}]<<<>[]>[{}[]]>))([[[<>{}]{[]()}][({}())>][[[<><>]]{({}())[<>{}]}]
{<[[[<[[{[[{((<>{})[()()])[<<>>{()<>}]}]]{{{<(<>{})<[][]>>[{<>{}}{{}[]}]}({{[]<>}(<>())}<<[]{}>>)
{<{<<({<<(([([(){}][()<>])[{[][]}(()[])]]{((()())[[]<>])})][[[[<[]{}>[<><>]][[()()][<>]]]({[{}{}]([]()
{[<([(({<<[<{<()><[]{}>}><((()[]))<[()][{}{}]>>](([[()[]][<><>]][({}[])[()[]]])<<{{}{}}<[]<>>>{[(
{[([{<{[<<[({{[]{}}<<><>>}{{()<>}<[]{}>}){{{[]<>]<{}[]>}[(()[])]}][(<[{}]>{([]<>)[[]{}]}){{[[]<>]}<{()
<({{{({[(<<<{<()[]>({}[])}{[()()]{[]<>}}>(<[[]()][<><>]>{([])<<>()>})>({{<{}()>(())}(({}){()<>})}[<<{}{}>{()
<({[({[(<[(<[(()())][([])[{}]]>{{{<><>}(<>{})}(([]{})<()()>)})]>[(([{((){})(<>()}}[([][]){[]}]](([{}[]]<
[<({([{{(<<<<({}())>>{{<<><>><<><>>}[({}<>){<><>}]}>[<{<[]{}>{[]()}}<[[]][[]()]>><[{{}<>}<()
{<<<([<<[[{([<()[]>{[]()}](<<>{}>([]<>))){<<{}{}><{}{}>><<[][]>({}{})>}}{<[<[][]>[<>()]]{[()[]]{[][]}}><<{<>}
<({[[<[{<(({{(()<>){{}<>}}[<()<>>({}[])]}<(<<>[]>{()()})[<[]{}>(()<>)]>)[<<{[]<>}(()<>)>[{(){}}<{}()>]>{({
(<([{{{<{({[<{()[]}{{}()}>]})}](<{(<<<[]{}>({}{})>[(()<>){[]{}}]>{({{}()}{{}<>})(<()()>[<>{}])})[([[{}<
((<(<<[((<{{[<<><>>{()<>}]([<>[]]<()<>>)}}><[(<{[]{}}{<><>}>{<{}{}>(()())})][[{[{}()][<>()]}((<><>)[<>[
([[[([<<{((<<({}[])(<>{})><({}())[<>[]]>>){((<[][]>([]<>)){{(){}]<<>[]>}){[{<><>}[{}{}]]}}){{{[{<>()}({}[])]<
<{{[{[<<[<{<<(()())(<>())>((<>[]))>[{[()()](<>()}}{({}<>)(<>{})}]}>]>{[<[{[{<>{}}{{}[]}]}{[<<><>>({}())](((
{<{[(<[(({<<{[{}[]](<><>)}<<()[]><{}<>>>><(((){})[{}])<[<>()]<()<>>>>>[{<[{}<>]<<>[]>>(<[]()>(<
[<<[[{[({(<((({}{})(<>())))[{{[]<>}<(){}>}]>([({{}<>}[[]{}])]((({}())(<>[]))([[]<>](()[])))))}[<(((({}()){<>[
{<((((({((<[{[[][]](<><>)}{{{}{}}(()())}]{((<><>)<[]()>)<<()<>>(()<>)>}>[{([{}()]<[]<>>){<[]<>><(){}
([{[<[<((<[<<{{}()}<<>{}>>([<><>]([]{}))>}(<{([]()){<>()}}[<[]<>>(<><>)]><(<()[]><()<>>)<[{}[]]
<<{[[<{{[({[{{{}{}}(()[])}]})]}([{[{([()]({}{}))[([][])<()[]>]}({{[][]}{[][]>}([()()]))][<(
<<{{[[<([{{({[()())(<><>)})}}{(<([<>()][[]<>])[{()[]}{{}{}}]>({{<>()}{{}<>}}))[({<[]><<>>}((<>()
{<<<({[<<[{((<{}[]>([][])))[([{}{}]<{}{}>){[()()](()<>)}]}{<{(<>())<{}<>>}([[]()]({}))>{[(<>[]
(<<[{[({{{<{[<[][]><[]()>][{()[]}[<>[]]]}><<[(<><>)<[][]>]<<<>{}><[]<>>>>({<{}()>([]<>)}({()[]}
[<<[<[[(<{[{[[{}[]]{()<>}]<[{}{}][{}()]>}{(<{}<>>{()[]})<{()[]}[[]()]>}]}{{<((<>{})[{}()])[{<><>}<[][]>]>[<{
{<<{([({<(<{(<[]<>>)}[<{[][]}>((<><>)((){}))]>)[(<{([]())[{}()]}<({})>>(<[()<>][[][]]>{([][])<()[]>})){[{<
{<(([{<<[[[({{[]{}}({}<>)}[(<>{})[<>[]]])({[()[]]{[]}]<[<><>]<[]{}>>)][(<[[]()]([]<>)>(([]())({}
(<[{([<([(<{{{<><>}<<>[]>}{[<><>][()<>]}}[(<[][]><()<>>)]>[{((()<>)<[]()))[(<><>)<()[]>]}])]<([<<{<>()
<[(<({{({[<{({<><>}[[][]]){((){})<()[]>}}{[{[]{}}{(){}}][{{}()}{()<>}]}><{[<{}[]>((){})]({<>
({<({(([{<{{<[<><>]{[][]}>[{()()}(()[])}}{<<<>{}>[{}{}]><{[]<>}[[][]]>}}[[{{<>{}}}<{<>[]}{(){}}>][{[(
<{[<[([<({[[{<<>{}>{<><>}}((()<>)<()()>)]<{[[]()]({}[])}<(<>())<()[]>>>>{{{{[]{}}[{}[]]}}([
<[(([{[[({{{{(()())<()()>}(<<>{}>{[]{}})}<{[<><>][<>()]}<{{}{}}>>}{[(<<>{}>((){}))[<[]()>{
{<<(<(({[<[{[((){})([][])]}{<(<>{}}(<>{})>[([]<>)([][])]}]{[<((){})<()<>>><<[]<>><{}()>>]({(()<>)}{<{}<
[[[(([([[[[[{[[]]}{({})(<>{})}){({{}}[{}[]]){<(){}><[]<>>}}]]]]){(([{(<<{}[]>(<><>)>)<<{{}[]}[<><
([(<(((({{[<({[]<>})(([])[{}[]])>[[<<>()>[<>()]][[[][]][[][]]]]]{<<([][]){()[])>(<{}{}>[[]
([(([(<<([[{{<{}<>>(<>[])}[[[]<>]<()()>]}[(({}<>){<>{}})[<[][]>[[][]]]]]{[{({}[])}<(<><>)[()<>]
{(<<(<[({(<[{[(){}]<<>()>}[[{}<>]{[]{}}]]><<[(()<>){[]{}}]{{[]}{<>}}>[[(<><>)]<(<>{}){{}{}}]]>)}([<{({(
[{<<<[{(<{(<<<(){}>[<>[]]>[{[][]}<<>{}>]>)<<[{(){}}{()<>}]<<()[]>]>([[[]()]<{}[]>](<<>()><<><>>))>}>)({[<<[
{<[([[([({([[(<>{})][([]()){[][]}]]{(<<><>>[()<>])<<{}<>>[()]>})})]{<[<((({}<>){{}{}}){<[]()>[<
<[<<([(((<<<([{}{}][<>()])>>{[[<()()>([]<>)]({<>{}}<{}{}>)]([(<><>)([]<>}]{{()<>}{{}[]}})}>{[[{{[]<>}<
<[{{{[<([[{[{[()[]]}(({}()){[]()})](({()}{{}()}){([]())<[]<>>}}}<{<([]())[()<>]>([[]()][{}{}]
<(<<<<{[{(({[{{}<>}[(){}]}}([(<>())]{[[]](<>{})}))(<[{{}<>}{<>()}][[[]{}]({}[])]>[(([]())<[]()>)[[()]{[
[<{[<<{[{{{[<{()[]}([]<>)>((<>{}))][[((){})[<>{}]]<(<>{})>]}}<({<{{}}[{}()])<(()<>)<{}{}>>}<<
<({<{{<{<[[(((()<>)[()()])[{[][]}<<>{}>])(<({}<>)(()<>)>[<<>{}>([]<>)])][{{[{}[]]((){})}([[][
<<<{{<<<<({(<{{}<>}<[]>>{<<><>>{[]{}}})<(<{}>({}<>)){{<>()}[()[]]}>]<{[<()<>>([]{})]{[(){}
(({<({[[{[{{{{{}{}}{<>{}}}[<<>{}><{}()>)}}]}(([{(<()()><{}()>)[{<>()}(<>())]}][[<{{}{}}({})>[<[]<>>
<{<<{[{[{(<([{<>[]}<()[]>]{{[]()}<{}[]>})<[[<>()]{()[]}](([][])[{}{}])>>)<({<({}[])[{}[]]>({[]{}}
(<([{{{(({({<{<><>}[{}<>]>})<{[(<>())[<>[]]]}{<(<>{}){{}()}>}>})(([((<[]()><[]()>))(<<()[]>{<>{}
<[[[{{[{<<[(({{}<>}<(){}>)[<{}{}>({}())])]<{<{{}[]}>}{([()]{<>{}})}>>>(<([(((){})[(){}])])(((<(){
[[[{{[{[([(<[{()<>}((){})]{[{}()][<><>]}>)([{<(){}>}({<>}[<>[]])]<{{{}()}(<>[])}<(()())([]'''

open_close = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

point = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
close_points = {
    ")": 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def parse_lines(input):
    expected_close = []
    for char in input:

        if char in open_close.keys():
            expected_close.append(open_close[char])
        elif char in open_close.values():
            if char != expected_close[-1]:
                return point[char]
            elif char == expected_close[-1]:
                expected_close.pop()

    return None


def get_corrupted_sum(input):
    point_values = [parse_lines(i) for i in input.split('\n')]
    return sum([n for n in point_values if n is not None])

def get_fill_closing(input):
    point_values = [fill_closing_chars(i) for i in input.split('\n') if fill_closing_chars(i) is not None]
    print(statistics.median(point_values))

def fill_closing_chars(input):
    expected_close = []

    for char in input:
        if char in open_close.keys():
            expected_close.append(open_close[char])
        elif char in open_close.values():
            # corrupted
            if char != expected_close[-1]:
                return None
            elif char == expected_close[-1]:
                expected_close.pop()

    return _calc_closing_score(expected_close)

def _calc_closing_score(expected_close:List[str]):
    total = 0
    for char in expected_close:
        total *= 5
        total += close_points[char]
    return total

if __name__ == '__main__':
    #print(get_corrupted_sum(test_input))
    #print(get_corrupted_sum(input))
    assert _calc_closing_score('}}]])})]') == 288957
    assert _calc_closing_score(')}>]})') == 5566
    assert _calc_closing_score('}}>}>))))') == 1480781
    assert _calc_closing_score(']]}}]}]}>') == 995444

    get_fill_closing(test_input)
    get_fill_closing(input)