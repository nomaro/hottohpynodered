# Project desciption

Based on Original work of benlbrm : HOTTOHPY

This library can be used to discuss with HootoH based stove devices

Actually tested and validated with a MCZ VIVO 90.

To use this library you need to have a wifi capable stove.

Install python's library :
```
pip3 install crcmod
pip3 install bitstring
pip3 install parse
```


Change IP adress in command.py

Set.py with arguments "flame:[0-5]/fan1:[0-6]/fan2:[0-6]/mode:[off|man|eco]/" send command to the stove.
example :
```
python3 command.py flame:1/fan1:0/fan2:1/mode:man/
```

# Flow in node-red

```
[{"id":"49c7f2cf.9cc2ec","type":"tab","label":"LOX <> MCZ WIFI","disabled":false,"info":""},{"id":"a404ba6d.6493b8","type":"change","z":"49c7f2cf.9cc2ec","name":"","rules":[{"t":"move","p":"payload","pt":"msg","to":"payload.flame","tot":"msg"}],"action":"","property":"","from":"","to":"","reg":false,"x":290,"y":40,"wires":[["e9f87d69.3ee41"]]},{"id":"1ed46340.ac5e9d","type":"file in","z":"49c7f2cf.9cc2ec","name":"","filename":"mczfan1","format":"utf8","chunk":false,"sendError":false,"encoding":"none","x":820,"y":80,"wires":[["213e0f67.917dc"]]},{"id":"ed7c52af.6c30d","type":"file in","z":"49c7f2cf.9cc2ec","name":"","filename":"mczfan2","format":"utf8","chunk":false,"sendError":false,"encoding":"none","x":820,"y":120,"wires":[["4e0cc14c.6bd3c"]]},{"id":"905b52c8.55da2","type":"file in","z":"49c7f2cf.9cc2ec","name":"","filename":"mczmode","format":"utf8","chunk":false,"sendError":false,"encoding":"none","x":820,"y":160,"wires":[["80d425e0.4ce4c8"]]},{"id":"cd376f60.536c","type":"file in","z":"49c7f2cf.9cc2ec","name":"","filename":"mczflame","format":"utf8","chunk":false,"sendError":false,"encoding":"none","x":820,"y":40,"wires":[["61561d5f.bbe6e4"]]},{"id":"e9f87d69.3ee41","type":"file","z":"49c7f2cf.9cc2ec","name":"","filename":"mczflame","appendNewline":false,"createDir":true,"overwriteFile":"true","encoding":"none","x":460,"y":40,"wires":[["53149f65.da99d"]]},{"id":"bcb1a531.409918","type":"file","z":"49c7f2cf.9cc2ec","name":"","filename":"mczfan1","appendNewline":false,"createDir":true,"overwriteFile":"true","encoding":"none","x":460,"y":80,"wires":[["53149f65.da99d"]]},{"id":"58895007.43a7b","type":"file","z":"49c7f2cf.9cc2ec","name":"","filename":"mczfan2","appendNewline":false,"createDir":true,"overwriteFile":"true","encoding":"none","x":460,"y":120,"wires":[["53149f65.da99d"]]},{"id":"caee4b89.e370d8","type":"file","z":"49c7f2cf.9cc2ec","name":"","filename":"mczmode","appendNewline":false,"createDir":true,"overwriteFile":"true","encoding":"none","x":460,"y":160,"wires":[["53149f65.da99d"]]},{"id":"213e0f67.917dc","type":"json","z":"49c7f2cf.9cc2ec","name":"","property":"payload","action":"","pretty":true,"x":950,"y":80,"wires":[["df1cc997.dbc9d8"]]},{"id":"4e0cc14c.6bd3c","type":"json","z":"49c7f2cf.9cc2ec","name":"","property":"payload","action":"","pretty":true,"x":950,"y":120,"wires":[["1fff02bc.64a75d"]]},{"id":"80d425e0.4ce4c8","type":"json","z":"49c7f2cf.9cc2ec","name":"","property":"payload","action":"","pretty":true,"x":950,"y":160,"wires":[["53ed5f1.771dea"]]},{"id":"61561d5f.bbe6e4","type":"json","z":"49c7f2cf.9cc2ec","name":"","property":"payload","action":"","pretty":true,"x":950,"y":40,"wires":[["534c08d2.81cdf8"]]},{"id":"53149f65.da99d","type":"trigger","z":"49c7f2cf.9cc2ec","name":"","op1":"","op2":"","op1type":"nul","op2type":"payl","duration":"700","extend":true,"overrideDelay":false,"units":"ms","reset":"","bytopic":"all","topic":"topic","outputs":1,"x":640,"y":100,"wires":[["cd376f60.536c","1ed46340.ac5e9d","ed7c52af.6c30d","905b52c8.55da2"]]},{"id":"690282b7.1730ec","type":"change","z":"49c7f2cf.9cc2ec","name":"","rules":[{"t":"move","p":"payload","pt":"msg","to":"payload.fan1","tot":"msg"}],"action":"","property":"","from":"","to":"","reg":false,"x":290,"y":80,"wires":[["bcb1a531.409918"]]},{"id":"6f796eab.6f636","type":"change","z":"49c7f2cf.9cc2ec","name":"","rules":[{"t":"move","p":"payload","pt":"msg","to":"payload.fan2","tot":"msg"}],"action":"","property":"","from":"","to":"","reg":false,"x":290,"y":120,"wires":[["58895007.43a7b"]]},{"id":"d78d7ba4.159bb8","type":"change","z":"49c7f2cf.9cc2ec","name":"","rules":[{"t":"change","p":"payload","pt":"msg","from":"0","fromt":"num","to":"off","tot":"str"},{"t":"change","p":"payload","pt":"msg","from":"1","fromt":"num","to":"man","tot":"str"},{"t":"change","p":"payload","pt":"msg","from":"2","fromt":"num","to":"eco","tot":"str"},{"t":"move","p":"payload","pt":"msg","to":"payload.mode","tot":"msg"}],"action":"","property":"","from":"","to":"","reg":false,"x":280,"y":159,"wires":[["caee4b89.e370d8"]]},{"id":"b453d0d6.4d6d7","type":"join","z":"49c7f2cf.9cc2ec","name":"","mode":"custom","build":"string","property":"payload","propertyType":"msg","key":"topic","joiner":"","joinerType":"str","accumulate":false,"timeout":"","count":"4","reduceRight":false,"reduceExp":"","reduceInit":"","reduceInitType":"num","reduceFixup":"","x":1510,"y":100,"wires":[["3f63c9cd.2c4d06"]]},{"id":"3f63c9cd.2c4d06","type":"exec","z":"49c7f2cf.9cc2ec","command":"cd /home/pi/hottohpy ; python3 command.py","addpay":true,"append":"","useSpawn":"false","timer":"","oldrc":false,"name":"","x":1750,"y":100,"wires":[["31ac41e7.11662e","4f7652d0.65bafc"],[],[]]},{"id":"31ac41e7.11662e","type":"debug","z":"49c7f2cf.9cc2ec","name":"","active":false,"tosidebar":true,"console":false,"tostatus":false,"complete":"false","statusVal":"","statusType":"auto","x":2070,"y":180,"wires":[]},{"id":"534c08d2.81cdf8","type":"change","z":"49c7f2cf.9cc2ec","name":"","rules":[{"t":"set","p":"payload","pt":"msg","to":"$string(payload)","tot":"jsonata"}],"action":"","property":"","from":"","to":"","reg":false,"x":1140,"y":40,"wires":[["41801fb6.95661"]]},{"id":"df1cc997.dbc9d8","type":"change","z":"49c7f2cf.9cc2ec","name":"","rules":[{"t":"set","p":"payload","pt":"msg","to":"$string(payload)\t","tot":"jsonata"}],"action":"","property":"","from":"","to":"","reg":false,"x":1140,"y":80,"wires":[["7622628e.15fc6c"]]},{"id":"1fff02bc.64a75d","type":"change","z":"49c7f2cf.9cc2ec","name":"","rules":[{"t":"set","p":"payload","pt":"msg","to":"$string(payload)\t","tot":"jsonata"}],"action":"","property":"","from":"","to":"","reg":false,"x":1140,"y":120,"wires":[["dfafc60e.25ff68"]]},{"id":"53ed5f1.771dea","type":"change","z":"49c7f2cf.9cc2ec","name":"","rules":[{"t":"set","p":"payload","pt":"msg","to":"$string(payload)\t","tot":"jsonata"}],"action":"","property":"","from":"","to":"","reg":false,"x":1140,"y":160,"wires":[["90bbe3c3.a5483"]]},{"id":"41801fb6.95661","type":"change","z":"49c7f2cf.9cc2ec","name":"","rules":[{"t":"change","p":"payload","pt":"msg","from":"{\"","fromt":"str","to":"","tot":"str"},{"t":"change","p":"payload","pt":"msg","from":"\":","fromt":"str","to":":","tot":"str"},{"t":"change","p":"payload","pt":"msg","from":"}","fromt":"str","to":"/","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":1320,"y":38,"wires":[["b453d0d6.4d6d7"]]},{"id":"7622628e.15fc6c","type":"change","z":"49c7f2cf.9cc2ec","name":"","rules":[{"t":"change","p":"payload","pt":"msg","from":"{\"","fromt":"str","to":"","tot":"str"},{"t":"change","p":"payload","pt":"msg","from":"\":","fromt":"str","to":":","tot":"str"},{"t":"change","p":"payload","pt":"msg","from":"}","fromt":"str","to":"/","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":1320,"y":80,"wires":[["b453d0d6.4d6d7"]]},{"id":"dfafc60e.25ff68","type":"change","z":"49c7f2cf.9cc2ec","name":"","rules":[{"t":"change","p":"payload","pt":"msg","from":"{\"","fromt":"str","to":"","tot":"str"},{"t":"change","p":"payload","pt":"msg","from":"\":","fromt":"str","to":":","tot":"str"},{"t":"change","p":"payload","pt":"msg","from":"}","fromt":"str","to":"/","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":1320,"y":120,"wires":[["b453d0d6.4d6d7"]]},{"id":"90bbe3c3.a5483","type":"change","z":"49c7f2cf.9cc2ec","name":"","rules":[{"t":"change","p":"payload","pt":"msg","from":"{\"","fromt":"str","to":"","tot":"str"},{"t":"change","p":"payload","pt":"msg","from":"\":","fromt":"str","to":":","tot":"str"},{"t":"change","p":"payload","pt":"msg","from":"}","fromt":"str","to":"/","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":1320,"y":160,"wires":[["b453d0d6.4d6d7"]]},{"id":"7e54d7f.1a23228","type":"loxone-control-in","z":"49c7f2cf.9cc2ec","name":"Fan1","miniserver":"ac6c4958.c74c48","control":"1282d941-02aa-ea3e-ffffe0f00812718d","state":"1282d941-02aa-ea67-ffffe0f00812718d","x":130,"y":80,"wires":[["690282b7.1730ec"]]},{"id":"20001de1.b085f2","type":"loxone-control-in","z":"49c7f2cf.9cc2ec","name":"Fan2","miniserver":"ac6c4958.c74c48","control":"1282d7ec-00f7-797a-fffffb4a8841ecd4","state":"1282d7ec-00f7-79a3-fffffb4a8841ecd4","x":130,"y":120,"wires":[["6f796eab.6f636"]]},{"id":"59a95efd.3e91d","type":"loxone-control-in","z":"49c7f2cf.9cc2ec","name":"Flame","miniserver":"ac6c4958.c74c48","control":"1282dacf-028f-0768-ffff41a0eb444028","state":"1282dacf-028f-0791-ffff41a0eb444028","x":130,"y":40,"wires":[["a404ba6d.6493b8"]]},{"id":"e28fbd36.6af61","type":"loxone-control-in","z":"49c7f2cf.9cc2ec","name":"Mode","miniserver":"ac6c4958.c74c48","control":"1529ce92-0161-3d57-ffffb7b764432087","state":"1529ce92-0161-3d88-ffffb7b764432087","x":130,"y":160,"wires":[["d78d7ba4.159bb8"]]},{"id":"741fa17.1d1e46","type":"loxone-control-out","z":"49c7f2cf.9cc2ec","name":"EcoMode","miniserver":"ac6c4958.c74c48","control":"1bf36f49-0262-1eba-ffff41f8ecfa7d9e","x":2540,"y":140,"wires":[]},{"id":"9e0ab4a8.432f48","type":"loxone-control-out","z":"49c7f2cf.9cc2ec","name":"State","miniserver":"ac6c4958.c74c48","control":"1bf36f47-0360-c295-ffff41f8ecfa7d9e","x":2530,"y":60,"wires":[]},{"id":"4c90a040.14c4c","type":"loxone-control-out","z":"49c7f2cf.9cc2ec","name":"StoveIsOn","miniserver":"ac6c4958.c74c48","control":"1bf36f4a-015a-7ae2-ffff41f8ecfa7d9e","x":2550,"y":100,"wires":[]},{"id":"3d511423.057a8c","type":"loxone-control-out","z":"49c7f2cf.9cc2ec","name":"Fan1","miniserver":"ac6c4958.c74c48","control":"1bf37011-019e-1b0d-ffff41f8ecfa7d9e","x":2530,"y":220,"wires":[]},{"id":"e1a72ab6.21b7d8","type":"loxone-control-out","z":"49c7f2cf.9cc2ec","name":"Fan2","miniserver":"ac6c4958.c74c48","control":"1bf37027-03cd-302d-ffff41f8ecfa7d9e","x":2530,"y":260,"wires":[]},{"id":"e5de4def.23639","type":"loxone-control-out","z":"49c7f2cf.9cc2ec","name":"Flamme","miniserver":"ac6c4958.c74c48","control":"1bf36ff3-03de-a64a-ffff41f8ecfa7d9e","x":2540,"y":180,"wires":[]},{"id":"97431a95.35f028","type":"loxone-control-out","z":"49c7f2cf.9cc2ec","name":"T Fumée","miniserver":"ac6c4958.c74c48","control":"1bf36ff5-0362-0278-ffff41f8ecfa7d9e","x":2540,"y":300,"wires":[]},{"id":"c0c00bed.13a8b8","type":"switch","z":"49c7f2cf.9cc2ec","name":"","property":"payload","propertyType":"msg","rules":[{"t":"cont","v":"get_naction","vt":"str"},{"t":"cont","v":"_getStoveIsOn","vt":"str"},{"t":"cont","v":"_getEcoMode","vt":"str"},{"t":"cont","v":"_getSetPowerLevel","vt":"str"},{"t":"cont","v":"_getSetSpeedFan1","vt":"str"},{"t":"cont","v":"_getSetSpeedFan2","vt":"str"},{"t":"cont","v":"_getSmokeTemperature","vt":"str"}],"checkall":"true","repair":false,"outputs":7,"x":2170,"y":100,"wires":[["63b3cb4c.149894"],["ca4b719.820b29"],["ef6129b2.155018"],["b30ab39.320635"],["ed500e12.16ad5"],["d7e57a63.337308"],["a30b9333.dae8c"]]},{"id":"4f7652d0.65bafc","type":"split","z":"49c7f2cf.9cc2ec","name":"","splt":"\\n","spltType":"str","arraySplt":1,"arraySpltType":"len","stream":false,"addname":"","x":2050,"y":100,"wires":[["c0c00bed.13a8b8"]]},{"id":"63b3cb4c.149894","type":"change","z":"49c7f2cf.9cc2ec","name":"","rules":[{"t":"change","p":"payload","pt":"msg","from":"get_naction:","fromt":"str","to":"","tot":"str"},{"t":"change","p":"payload","pt":"msg","from":" ","fromt":"str","to":"","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":2380,"y":60,"wires":[["9e0ab4a8.432f48"]]},{"id":"ca4b719.820b29","type":"change","z":"49c7f2cf.9cc2ec","name":"","rules":[{"t":"change","p":"payload","pt":"msg","from":"_getStoveIsOn:","fromt":"str","to":"","tot":"str"},{"t":"change","p":"payload","pt":"msg","from":" ","fromt":"str","to":"","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":2380,"y":100,"wires":[["4c90a040.14c4c"]]},{"id":"ef6129b2.155018","type":"change","z":"49c7f2cf.9cc2ec","name":"","rules":[{"t":"change","p":"payload","pt":"msg","from":"_getEcoMode:","fromt":"str","to":"","tot":"str"},{"t":"change","p":"payload","pt":"msg","from":" ","fromt":"str","to":"","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":2380,"y":140,"wires":[["741fa17.1d1e46"]]},{"id":"b30ab39.320635","type":"change","z":"49c7f2cf.9cc2ec","name":"","rules":[{"t":"change","p":"payload","pt":"msg","from":"_getSetPowerLevel:","fromt":"str","to":"","tot":"str"},{"t":"change","p":"payload","pt":"msg","from":" ","fromt":"str","to":"","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":2380,"y":180,"wires":[["e5de4def.23639"]]},{"id":"ed500e12.16ad5","type":"change","z":"49c7f2cf.9cc2ec","name":"","rules":[{"t":"change","p":"payload","pt":"msg","from":"_getSetSpeedFan1:","fromt":"str","to":"","tot":"str"},{"t":"change","p":"payload","pt":"msg","from":" ","fromt":"str","to":"","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":2380,"y":220,"wires":[["3d511423.057a8c"]]},{"id":"d7e57a63.337308","type":"change","z":"49c7f2cf.9cc2ec","name":"","rules":[{"t":"change","p":"payload","pt":"msg","from":"_getSetSpeedFan2:","fromt":"str","to":"","tot":"str"},{"t":"change","p":"payload","pt":"msg","from":" ","fromt":"str","to":"","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":2380,"y":260,"wires":[["e1a72ab6.21b7d8"]]},{"id":"a30b9333.dae8c","type":"change","z":"49c7f2cf.9cc2ec","name":"","rules":[{"t":"change","p":"payload","pt":"msg","from":"_getSmokeTemperature:","fromt":"str","to":"","tot":"str"},{"t":"change","p":"payload","pt":"msg","from":" ","fromt":"str","to":"","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":2380,"y":300,"wires":[["97431a95.35f028"]]},{"id":"106e1a17.d22c76","type":"cronplus","z":"49c7f2cf.9cc2ec","name":"","outputField":"payload","timeZone":"","persistDynamic":false,"commandResponseMsgOutput":"output1","outputs":1,"options":[{"name":"ping poele","topic":"ping poele","payloadType":"default","payload":"","expressionType":"cron","expression":"0 * * * * * ","location":"","offset":"0","solarType":"all","solarEvents":"sunrise,sunset"}],"x":460,"y":200,"wires":[["53149f65.da99d"]]},{"id":"ac6c4958.c74c48","type":"loxone-miniserver","host":"192.168.0.10","port":"80","enctype":"0","active":true,"keepalive":"5000"}]
```
