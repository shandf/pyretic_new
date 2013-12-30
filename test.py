def travel(node v,ip src,policy):
    ret=false
    policy=[]
    for child in childs of v:
        if(travel(child)):
            ret=true
            policy.append((src,v,fwd(child_port)))
    for host in hosts of v:
        if(host is in lst_lst):
            ret=true
            policy.append((src,v,fwd(host_port)))
    return ret
    #1
    mst=minimum_spanning_tree(self.network.topology)
    #2
    v=start_host
    travel(v,ip,src,policy)
    #3
    fun(policy,xxx)
    return xxx

((10.0.0.1,2,(1,2)),
(10.0.0.1,3,(1)),
...
)

====>

for term in policy:
    temp_port = drop 
    for port int set:
        temp_port =  temp_port + fwd(port)
    temp_policy=match(src='10.0.0.1',switch=2)>>fwd(temp_port)
    final_policy=final_policy+temp_policy

    def fun(policy,xxx):
        
        
    
