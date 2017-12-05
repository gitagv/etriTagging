from pymongo import MongoClient

client = MongoClient('mongodb://root:nlp44342@203.255.81.46')

db = client.etri_wiki

col = db['submit']

def main():
    for a in col.find():
        temp = ""
        # titleText = a['title']['text']
        titleText = a['title']['text']
        fileName = titleText+'.json'
        file = open(fileName, 'w', encoding='utf-8')
        print(titleText)

        temp += '{"doc_id" : "'
        temp += a['doc_id']
        temp += '",\n'

        temp += ' "DCT" : "'
        temp += a['DCT']
        temp += '",\n'

        temp += ' "category" : "'
        temp += a['category']
        temp += '",\n'

        temp += ' "category_weight" : '
        temp += str(a['category_weight'])
        temp += ',\n'

        temp += ' "title" : {"text" : "'
        temp += a['title']['text']
        temp += '", "NE" : "'
        temp += a['title']['NE']
        temp += '"},\n'

        temp += ' "metaInfo" : { },\n'

        senSize = len(a['sentence'])
        temp += ' "sentence" : [\n'
        for b in a['sentence']:
            temp += '\t{\n\t"id" : '
            temp += str(b['id'])
            temp += ',\n'

            temp += '\t"reserve_str" : "'
            temp += ""
            temp += '",\n'

            temp += '\t"text" : "'
            if str(b['text']).count('"') > 0:
                temp += str(b['text']).replace('"', '\\"')
            else:
                temp += b['text']
            temp += '",\n'

            sSize = len(b['morp'])
            temp += '\t"morp" : [\n'
            for c in b['morp']:
                temp += '\t\t{"id" : '
                temp += str(c['id'])
                temp += ', "lemma" : "'
                if str(c['lemma']).count('"') > 0:
                    temp += str(c['lemma']).replace('"', '\\"')
                else:
                    temp += c['lemma']
                temp += '", "type" : "'
                temp += c['type']
                temp += '", "position" : '
                temp += str(c['position'])
                temp += ', "weight" : '
                temp += str(c['weight'])
                if sSize-1 == c['id']:
                    temp += ' }\n'
                else:
                    temp += ' },\n'
            temp += '\t],\n'

            sSize = len(b['morp_eval'])
            temp += '\t"morp_eval" : [\n'
            for c in b['morp_eval']:
                temp += '\t\t{"id" : '
                temp += str(c['id'])
                temp += ', "result" : "'
                if str(c['result']).count('"') > 0:
                    temp += str(c['result']).replace('"', '\\"')
                else:
                    temp += c['result']
                temp += '", "target" : "'
                if str(c['target']).count('"') > 0:
                    temp += str(c['target']).replace('"', '\\"')
                else:
                    temp += c['target']
                temp += '", "word_id" : '
                temp += str(c['word_id'])
                temp += ', "m_begin" : '
                temp += str(c['m_begin'])
                temp += ', "m_end" : '
                temp += str(c['m_end'])
                if sSize-1 == c['id']:
                    temp += '}\n'
                else:
                    temp += '},\n'
            temp += '\t],\n'

            sSize = len(b['WSD'])
            temp += '\t"WSD" : [\n'
            for c in b['WSD']:
                temp += '\t\t{"id" : '
                temp += str(c['id'])
                temp += ', "text" : "'
                if str(c['text']).count('"') > 0:
                    temp += str(c['text']).replace('"', '\\"')
                else:
                    temp += c['text']
                temp += '", "type" : "'
                temp += c['type']
                temp += '", "scode" : "'
                temp += str(c['scode'])
                temp += '", "weight" : '
                temp += str(c['weight'])
                temp += ', "position" : '
                temp += str(c['position'])
                temp += ', "begin" : '
                temp += str(c['begin'])
                temp += ', "end" : '
                temp += str(c['end'])
                if sSize-1 == c['id']:
                    temp += '}\n'
                else:
                    temp += '},\n'
            temp += '\t],\n'

            sSize = len(b['word'])
            temp += '\t"word" : [\n'
            for c in b['word']:
                temp += '\t\t{"id" : '
                temp += str(c['id'])
                temp += ', "text" : "'
                if str(c['text']).count('"') > 0:
                    temp += str(c['text']).replace('"', '\\"')
                else:
                    temp += c['text']
                temp += '", "type" : "'
                temp += c['type']
                temp += '", "begin" : '
                temp += str(c['begin'])
                temp += ', "end" : '
                temp += str(c['end'])
                if sSize-1 == c['id']:
                    temp += '}\n'
                else:
                    temp += '},\n'
            temp += '\t],\n'

            sSize = len(b['NE'])
            temp += '\t"NE" : [\n'
            for c in b['NE']:
                temp += '\t\t{"id" : '
                temp += str(c['id'])
                temp += ', "text" : "'
                temp += c['text']
                temp += '", "type" : "'
                temp += c['type']
                temp += '", "begin" : '
                temp += str(c['begin'])
                temp += ', "end" : '
                temp += str(c['end'])
                temp += ', "weight" : '
                temp += str(c['weight'])
                temp += ', "common_noun" : '
                temp += str(c['common_noun'])
                if sSize-1 == c['id']:
                    temp += '}\n'
                else:
                    temp += '},\n'
            temp += '\t],\n'

            sSize = len(b['chunk'])
            temp += '\t"chunk" : [\n'
            for c in b['chunk']:
                continue
            temp += '\t],\n'

            sSize = len(b['dependency'])
            temp += '\t"dependency" : [\n'
            for c in b['dependency']:
                temp += '\t\t{"id" : '
                temp += str(c['id'])
                temp += ', "text" : "'
                if str(c['text']).count('"') > 0:
                    temp += str(c['text']).replace('"', '\\"')
                else:
                    temp += c['text']
                temp += '", "head" : '
                temp += str(c['head'])
                temp += ', "label" : "'
                temp += c['label']
                temp += '", "mod" : ['
                dSize = len(c['mod'])
                for dCount, d in enumerate(c['mod']):
                    temp += str(d)
                    if dSize-1 == dCount:
                        continue
                    else:
                        temp += ', '
                temp += '], "weight" : '
                temp += str(c['weight'])
                temp += ''
                if sSize-1 == c['id']:
                    temp += ' }\n'
                else:
                    temp += ' },\n'
            temp += '\t],\n'


            sSize = len(b['SRL'])
            temp += '\t"SRL" : [\n'
            for srlCount, c in enumerate(b['SRL']):
                temp += '\t\t{"verb" : "'
                temp += c['verb']
                temp += '", "sense" : '
                temp += str(c['sense'])
                temp += ', "word_id" : '
                temp += str(c['word_id'])
                temp += ', "weight" : '
                temp += str(c['weight'])
                temp += ',\n'
                aSize = len(c['argument'])
                temp += '\t\t\t"argument" : [\n'
                for dCount, d in enumerate(c['argument']):
                    temp += '\t\t\t\t{"type" : "'
                    temp += d['type']
                    temp += '", "word_id" : '
                    temp += str(d['word_id'])
                    temp += ', "text" : "'
                    if str(d['text']).count('"') > 0:
                        temp += str(d['text']).replace('"', '\\"')
                    else:
                        temp += d['text']
                    temp += '", "weight" : '
                    temp += str(d['weight'])
                    if aSize-1 == dCount:
                        temp += ' }\n'
                    else:
                        temp += ' },\n'
                if sSize-1 == srlCount:
                    temp += '\t\t\t] }\n'
                else:
                    temp += '\t\t\t] },\n'
            #     \t확인
            temp += '\t],\n'

            sSize = len(b['relation'])
            temp += '\t"relation" : [\n'
            for c in b['relation']:
                continue
            temp += '\t],\n'

            sSize = len(b['SA'])
            temp += '\t"SA" : [\n'
            for c in b['SA']:
                continue
            temp += '\t],\n'

            sSize = len(b['ZA'])
            temp += '\t"ZA" : [\n'
            for c in b['ZA']:
                temp += '\t\t{"id" : '
                temp += str(c['id'])
                temp += ', "verb_wid" : '
                temp += str(c['verb_wid'])
                temp += ', "ant_sid" : '
                temp += str(c['ant_sid'])
                temp += ', "ant_wid" : '
                temp += str(c['ant_wid'])
                temp += ', "type" : "'
                temp += c['type']
                temp += '", "istitle" : '
                temp += str(c['istitle'])
                temp += ', "weight" : '
                temp += str(c['weight'])
                if sSize-1 == c['id']:
                    temp += ' }\n'
                else:
                    temp += ' },\n'
            temp += '\t]\n'
            if senSize-1 == b['id']:
                temp += '\t}\n'
            else:
                temp += '\t},\n'
        temp += ' ],\n'

        temp += ' "entity" : [\n'
        temp += ' ]\n'

        temp += '}\n'
        temp += '\n'

        file.write(temp)
        file.close()

    # print(temp)
main()