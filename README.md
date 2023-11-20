# Interchain Relayers

A repository of all interchain relayers (IBC). Data stored in this repository is used to build https://relayers.smartstake.io

If you run relayer on any of the IBC chains, your relayer will be shown on Interchain Relayers dashboard after you create/update your relayer configuration based on below details.


# Instructions to configure your relayers

 1. If you dont have a keybase.io identity, make sure you set up one (ideally with a logo). Note down your 16 character keybase identity.
 2. Fork this repository
 3. In your own instance of the repository, locate your <identity>.json file in relayers folder
 4. If &lt;identity&gt;.json file is present, review the information and update details. If file is not present, create the file (e.g. DD01D013A474ACA3.json) and add details. The JSON file has below given structure (see sample values & explanation). Please note that chains relayed attribute will support all IBC chains irrespective of whether Smart Stake is a validator or not for that chain (chains validated is pulled from on chain data and is not part of this template). Please pay attention to the case of attributes (e.g. relayerAddress is the correct attribute name and relayeraddress is wrong)
 ```   
 {
    	"keybaseIdentity": "DD01D013A474ACA3",
    	"name": "Relayer/Validator Name",
    	"website": "enter your website",
    	"twitter": "yourprofilehandle", # @ not needed. full website address is not needed
    	"telegram": "tguserorgrouphandle", #does not support multiple TG handles. full website address is not needed
    	"discord": "discordhandle", #does not support multiple discord handles. full website address is needed
    	"email": "support@validator.example,
    	"supportRelayerBy": "what can community do to support you? a response like 'delegate to validator' or 'donate to relayer' is good. max of 50 characters",
    	"chainsRelayed": [
    		{"ticker": "ATOM", "relayerAddress": "cosmos...."},
    		{"ticker": "OSMO", "relayerAddress": "osmoaddr1...."},
    		{"ticker": "OSMO", "relayerAddress": "osmoaddr2...."}, #for multiple relaying addresses, make separate entry for network-address combination 
    		{"ticker": "INJ", "relayerAddress": "inj...."} #please make sure the last item doesnt end with a comma (it makes the json an invalid object)
    	]
 }
 ```
 5. Commit changes to your branch
 6. Open a pull request
 7. In case of delays in your changes getting accepted/rejected (give it 1 business day), reach out to Smart Stake support at https://t.me/SmartStake or https://t.me/bigb4ever
 8. Check your relayer profile on relayers.smartstake.io and make more changes as needed.
 
