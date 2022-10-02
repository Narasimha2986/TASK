import re


def show_Allocator():
    out = ''' Allocator-Name                  In-use/Allocated            Count
    ----------------------------------------------------------------------------
    AAA AttrL Hdr             :        816/65888      (  1%) [     17] Chunk
    AAA AttrL Sub             :       5848/65888      (  8%) [     17] Chunk
    AAA DB Elt Chun           :        144/65936      (  0%) [      1] Chunk
    AAA Unique Id Hash Table  :       8196/8288       ( 98%) [      1]
    AAA chunk                 :          0/256        (  0%) [      0] Chunk
    AAA chunk                 :          0/256        (  0%) [      0] Chunk
    AAA Interface Struct      :        492/584        ( 84%) [      1]
    Total allocated: 0.197 Mb, 202 Kb, 207096 bytes


    AAA Low Memory Statistics:
    __________________________
    Authentication low-memory threshold      : 3%
    Accounting low-memory threshold          : 2%
    AAA Unique ID Failure                    : 0
    Local server  Packet dropped             : 0
    CoA  Packet dropped                      : 0
    PoD  Packet dropped                      : 0
    '''
    # initial variables
    ret_dict = {}
    for line in out.splitlines():
        line = line.strip()

        # Allocator-Name                  In-use/Allocated            Count
        p1_0 = re.compile(r'^Allocator-Name\s+In-use\SAllocated\s+Count$')
        m = p1_0.match(line)

        if m:
            ret_dict['allocator'] = m.groupdict()
            continue
        # Allocator-Name                  In-use/Allocated            Count
        # AAA AttrL Hdr             :        816/65888      (  1%) [     17] Chunk
        # AAA AttrL Sub             :       5848/65888      (  8%) [     17] Chunk
        # AAA DB Elt Chun           :        144/65936      (  0%) [      1] Chunk
        # AAA Unique Id Hash Table  :       8196/8288       ( 98%) [      1]
        # AAA chunk                 :          0/256        (  0%) [      0] Chunk
        # AAA chunk                 :          0/256        (  0%) [      0] Chunk
        # AAA Interface Struct      :        492/584        ( 84%) [      1]
        # Total allocated: 0.197 Mb, 202 Kb, 207096 bytes
        p1_1 = re.compile(r'^(?P<Allocator_Name>\w.+)  : +(?P<Allocated>\S+) +(?P<Count>\D+\d.+)')
        m = p1_1.match(line)
        if m:
            allocator_name = m.groupdict()['Allocator_Name']
            allocated = m.groupdict()['Allocated']
            count = m.groupdict()['Count']
            if 'allocator' not in ret_dict:
                ret_dict['allocator'] = {}
            if allocator_name not in ret_dict['allocator']:
                ret_dict['allocator'][allocator_name] = {}
            ret_dict['allocator'][allocator_name]['Allocator_Name'] = allocator_name
            ret_dict['allocator'][allocator_name]['Allocated'] = allocated
            ret_dict['allocator'][allocator_name]['Count'] = count
            continue

        p1_2 = re.compile(r'^Total\sallocated\S\s+(?P<total>\w.+)$')
        m = p1_2.match(line)
        if m:
            total = m.groupdict()['total']
            if 'allocator' not in ret_dict:
                ret_dict['allocator'] = {}
            if total not in ret_dict:
                ret_dict['allocator']["Total allocated"]=total

        p3 = re.compile(r'^AAA +Low +Memory +Statistics:')
        m = p3.match(line)
        if m:
            ret_dict['AAA Low Memory Statistics'] = m.groupdict()
            continue

        # Authentication low-memory threshold : 3%
        p4 = re.compile(r'^Authentication +low-memory +threshold\s+:(?P<total> \d+\%$)')
        m = p4.match(line)
        if m:
            if 'AAA Low Memory Statistics' not in ret_dict:
                ret_dict['AAA Low Memory Statistics'] = {}
            ret_dict['AAA Low Memory Statistics']['Authentication_low-memory_threshold'] = m.groupdict()['total']
            continue
        p5 = re.compile(r'^Accounting +low-memory +threshold\s+:(?P<total> \d+\%$)')
        m = p5.match(line)
        if m:
            if 'AAA Low Memory Statistics' not in ret_dict:
                ret_dict['AAA Low Memory Statistics'] = {}
            ret_dict['AAA Low Memory Statistics']['Accounting_low-memory_threshold'] = m.groupdict()['total']
            continue
        p6 = re.compile(r"^AAA +Unique +ID +Failure\s+:(?P<total> \d+)$")
        m = p6.match(line)
        if m:
            if 'AAA Low Memory Statistics' not in ret_dict:
                ret_dict['AAA Low Memory Statistics'] = {}
            ret_dict['AAA Low Memory Statistics']['AAA_Unique_ID_Failure'] = m.groupdict()['total']
            continue
        p7 = re.compile(r"^Local +server  +Packet +dropped\s+:(?P<total> \d+)$")
        m = p7.match(line)
        if m:
            if 'AAA Low Memory Statistics' not in ret_dict:
                ret_dict['AAA Low Memory Statistics'] = {}
            ret_dict['AAA Low Memory Statistics']['Local _erver_Packet_dropped'] = m.groupdict()['total']
            continue
        p8 = re.compile(r"^CoA  +Packet +dropped\s+:(?P<total> \d+)$")
        m = p8.match(line)
        if m:
            if 'AAA Low Memory Statistics' not in ret_dict:
                ret_dict['AAA Low Memory Statistics'] = {}
            ret_dict['AAA Low Memory Statistics']['CoA _Packet_dropped'] = m.groupdict()['total']
            continue
        p9 = re.compile(r"^PoD  +Packet +dropped\s+:(?P<total> \d+)")
        m = p9.match(line)
        if m:
            if 'AAA Low Memory Statistics' not in ret_dict:
                ret_dict['AAA Low Memory Statistics'] = {}
            ret_dict['AAA Low Memory Statistics']['PoD_Packet_dropped'] = m.groupdict()['total']
            continue

    return ret_dict


value = show_Allocator()
print(value)
##########################################output#################################################
{
   "allocator":{
      "AAA AttrL Hdr           ":{
         "Allocator_Name":"AAA AttrL Hdr           ",
         "Allocated":"816/65888",
         "Count":"(  1%) [     17] Chunk"
      },
      "AAA AttrL Sub           ":{
         "Allocator_Name":"AAA AttrL Sub           ",
         "Allocated":"5848/65888",
         "Count":"(  8%) [     17] Chunk"
      },
      "AAA DB Elt Chun         ":{
         "Allocator_Name":"AAA DB Elt Chun         ",
         "Allocated":"144/65936",
         "Count":"(  0%) [      1] Chunk"
      },
      "AAA Unique Id Hash Table":{
         "Allocator_Name":"AAA Unique Id Hash Table",
         "Allocated":"8196/8288",
         "Count":"( 98%) [      1]"
      },
      "AAA chunk               ":{
         "Allocator_Name":"AAA chunk               ",
         "Allocated":"0/256",
         "Count":"(  0%) [      0] Chunk"
      },
      "AAA Interface Struct    ":{
         "Allocator_Name":"AAA Interface Struct    ",
         "Allocated":"492/584",
         "Count":"( 84%) [      1]"
      },
      "Total allocated":"0.197 Mb, 202 Kb, 207096 bytes"
   },
   "AAA Low Memory Statistics":{
      "Authentication_low-memory_threshold":" 3%",
      "Accounting_low-memory_threshold":" 2%",
      "AAA_Unique_ID_Failure":" 0",
      "Local _erver_Packet_dropped":" 0",
      "CoA _Packet_dropped":" 0",
      "PoD_Packet_dropped":" 0"
   }
}