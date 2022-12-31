import 'dart:math';
import 'dart:core';
// import "package:collection/collection.dart";

const String test_template = "NNCB";
const String test_input_instructions = """
CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C""";

const String template = "SCSCSKKVVBKVFKSCCSOV";
const String instructions = """
CP -> C
SF -> S
BH -> F
SS -> N
KB -> N
NO -> N
BP -> F
NK -> P
VP -> H
OF -> O
VH -> O
FV -> F
OP -> V
FP -> B
VB -> B
OK -> S
BS -> B
SK -> P
VV -> H
PC -> S
HV -> K
PS -> N
VS -> O
HF -> B
SV -> C
HP -> O
NF -> V
HB -> F
VO -> B
VN -> N
ON -> H
KV -> K
OV -> F
HO -> H
NB -> K
CB -> F
FF -> H
NH -> F
SN -> N
PO -> O
PH -> C
HH -> P
KF -> N
OH -> N
KS -> O
FH -> H
CC -> F
CK -> N
FC -> F
CF -> H
HN -> B
OC -> F
OB -> K
FO -> P
KP -> N
NC -> P
PN -> O
PV -> B
CO -> C
CS -> P
PP -> V
FN -> B
PK -> C
VK -> S
HS -> P
OS -> N
NP -> K
SB -> F
OO -> F
CV -> V
BB -> O
SH -> O
NV -> N
BN -> C
KN -> H
KC -> C
BK -> O
KO -> S
VC -> N
KK -> P
BO -> V
BC -> V
BV -> H
SC -> N
NN -> C
CH -> H
SO -> P
HC -> F
FS -> P
VF -> S
BF -> S
PF -> O
SP -> H
FK -> N
NS -> C
PB -> S
HK -> C
CN -> B
FB -> O
KH -> O""";

 print_min_max(Map<String,int>Counter){
  List<int> values = Counter.values.toList();
  int largest = values.reduce(max);
  int smallest = values.reduce(min);

  print(largest-smallest);
}

Map<String,int> count_elements (String input){
  Map<String,int> result= {};

  input.split('').forEach((letter) {
    if (result[letter]==null){
      result[letter]=1;
    } else{
      result[letter] = result[letter]!+1;
    }
  });
  return result;

}

Map<String, String> translate_instructions(String input) {
  var m = input.split("\n");

  Map<String, String> ins = {};
  m.forEach((element) {
    var s = element.split('->');
    ins[s[0].trim()] = s[1].trim();
  });

  return ins;
}

List<String> toChunks(String template){
  List<String> chunks = [];

  int index = 0;
  while (index+2 <= template.length){
    chunks.add(template.substring(index,index+2));
    index++;
  }
  return chunks;
}

int solve(String template, Map instructions, int iterations) {

  // split into initial chunks

  // apply instructions multiple times
  for (int i=0; i < iterations; i++){

    int index = 0;
    List<String> updatedTemplate = [];
    while (index+2 <= template.length){
      String pair = template.substring(index,index+2);
      String toAdd = instructions[pair];

      updatedTemplate.addAll([pair.substring(0,1),toAdd]);
      index++;
    }

    updatedTemplate.add(template.substring(template.length-1,template.length));
    template = updatedTemplate.join("");
    print("Iteration: $i len:  ${updatedTemplate.length}");
    print(count_elements(template));
    print_min_max(count_elements(template));
    print(template);
  }
  // find the most common and least common letter
  var Counter = count_elements(template);
  List<int> values = Counter.values.toList();
  int largest = values.reduce(max);
  int smallest = values.reduce(min);

  print(largest-smallest);
  return largest-smallest;
}

void main() {

  solve(test_template,translate_instructions(test_input_instructions),10);
  // assert (solve(test_template,translate_instructions(test_input_instructions),40)==2188189693529);
  // solve(template, translate_instructions(instructions), 10);
}