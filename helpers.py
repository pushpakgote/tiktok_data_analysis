import json

def load_data():
    with open('tiktok_json.json','r') as f:
        data=json.load(f)
    return data

def check_type(data):
    if str(type(data)) in  ["<class 'dict'>","<class 'list'>"]:
        return True
    
def unroll_data(data,name,data_dict,rec_num):
    #print(rec_num)
    if rec_num>30:
        return data_dict
    #print(data_dict)
    if str(type(data))=="<class 'dict'>":
        #print('in dict')
        for key,values in data.items():
            if check_type(values):
                #print('going again',key,'   name : ',name)
                data_dict=unroll_data(values,name+[key],data_dict,rec_num+1)
            else:
                #print('key: ','_'.join(name+[key]),'    value: ',values)
                data_dict['_'.join(name+[key])] = values
                
    elif str(type(data))=="<class 'list'>":
        if check_type(data[0]):
            #print('going again list name : ',name)
            data_dict=unroll_data(data[0],name,data_dict,rec_num+1)
        else:
            #print('key: ','_'.join(name),'    value: ',data)
            data_dict['_'.join(name)]=data
            
    return data_dict
                

def process_result(data):
    #data=load_data()
    new_data=[]
    for tiktok_vid in data:
        name=[]
        del tiktok_vid['textExtra']
        del tiktok_vid['challenges']
        try:
            del tiktok_vid['video']['subtitleInfos']
        except:
            pass
        new_data.append( unroll_data(tiktok_vid,name,{},1) )  
        
    return new_data

    #with open("processed_tiktok.json", "w") as outfile:
    #    json.dump(new_data, outfile)
    
    