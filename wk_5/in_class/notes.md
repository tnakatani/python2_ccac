# APIs

## API fundamentals

IP address is an address of a host

### IP octets: 

```
# Example IP address
104 236 104 185 : 443
```
- Routing algorithms systematically forwards IP number to other routers.
- Can use tools like [traceroute-online.com](https://traceroute-online.com/) or ```traceroute``` in your terminal to trace the routing of requests

## NHTSA.gov API

NHTSA provides an API for complaints, recalls, safety ratings, etc.  You can directly query their database by requesting a URL that follows their format.

Example: Request recall info for Saturn LS 2000 models
```
curl https://webapi.nhtsa.gov/api/Recalls/vehicle/modelyear/2000/make/saturn/model/LS?format=json
```

The above request will return the following (with some extra formatting)

```json
{
  "Count": 6,
  "Message": "Results returned successfully",
  "Results": [
    {
      "Manufacturer": "GENERAL MOTORS CORP.",
      "NHTSACampaignNumber": "03V231000",
      "ReportReceivedDate": "/Date(1056340800000-0400)/",
      "Component": "ELECTRICAL SYSTEM:IGNITION:MODULE",
      "Summary": "ON CERTAIN PASSENGER VEHICLES EQUIPPED WITH 2.2L L4 (L61) ENGINES, A FAILURE OF THE IGNITION CONTROL MODULE MAY CAUSE DETERIORATION IN IDLE QUALITY, REDUCTION IN OVERALL ENGINE POWER, AND THE VEHICLE MAY BE HARD TO START.  CONTINUED OPERATION OF THE VEHICLE AFTER SUCH AN IGNITION MODULE FAILURE WILL RESULT IN THE \"SERVICE ENGINE SOON\" LIGHT FLASHING, AND MAY LEAD TO SECONDARY FAILURES OF THE CATALYTIC CONVERTER, OXYGEN SENSOR, AND EXHAUST RESONATOR.    \r\n",
      "Conequence": "FAILURE OF THE RESONATOR WILL CAUSE INCREASED EXHAUST NOISE.  PROLONGED OPERATION OF THE VEHICLE FOLLOWING A RESONATOR FAILURE MAY LEAD TO A  FIRE.  ",
      "Remedy": "DEALERS WILL (1) REPLACE THE IGNITION CONTROL MODULE, (2) REPLACE THE IGNITION CONTROL MODULE AND SPARK PLUGS, OR (3) REPLACE THE IGNITION CONTROL MODULE, SPARK PLUGS, AND UPDATE THE POWERTRAIN CONTROL MODULE CALIBRATION.   OWNER NOTIFICATION BEGAN ON AUGUST 4, 2003.  OWNERS SHOULD CONTACT SATURN AT 1-800-553-6000, PROMPT 3.   ",
      "Notes": "GM RECALL NO. 03033/SATURN RECALL NO. 03-C-06.  CUSTOMERS CAN ALSO CONTACT THE NATIONAL HIGHWAY TRAFFIC SAFETY ADMINISTRATION'S AUTO SAFETY HOTLINE AT 1-888-DASH-2-DOT (1-888-327-4236).",
      "ModelYear": "2000",
      "Make": "SATURN",
      "Model": "LS"
    },
    {
      "Manufacturer": "GENERAL MOTORS CORP.",
      "NHTSACampaignNumber": "05V245000",
      "NHTSAActionNumber": "PE05010",
      "ReportReceivedDate": "/Date(1117684800000-0400)/",
      "Component": "EXTERIOR LIGHTING:BRAKE LIGHTS",
      "Summary": "ON CERTAIN SEDANS AND WAGONS, THE PLASTIC HOUSING IN THE REAR TAIL LAMP ASSEMBLY CAN BECOME DISTORTED IF THE BRAKE LAMPS REMAIN ON FOR AN EXTENDED TIME.",
      "Conequence": "THIS CAN CAUSE (1) AN INTERMITTENTLY INOPERATIVE BRAKE/TAIL LAMP BULB OR (2) A SHORT CIRCUIT THAT OPENS A FUSE CAUSING INOPERATIVE BRAKE LAMPS (INCLUDING THE CENTER HIGH-MOUNTED STOP LAMP) OR TAIL LAMPS.  A FOLLOWING DRIVER MAY NOT KNOW WHEN THE BRAKES HAVE BEEN APPLIED, AND A REAR-END CRASH COULD OCCUR WITHOUT PRIOR WARNING.",
      "Remedy": "DEALERS WILL INSTALL TWO NEW TAIL LAMP REINFORCING SOCKET ADAPTERS AND SOCKETS FREE OF CHARGE.    THE RECALL BEGAN ON OCTOBER 17, 2005.  OWNERS MAY CONTACT SATURN AT 1-800-972-8876.",
      "Notes": "GM RECALL NO. 05052.  CUSTOMERS MAY ALSO CONTACT THE NATIONAL HIGHWAY TRAFFIC SAFETY ADMINISTRATION'S VEHICLE SAFETY HOTLINE AT 1-888-327-4236 (TTY 1-800-424-9153), OR GO TO HTTP://WWW.SAFERCAR.GOV.",
      "ModelYear": "2000",
      "Make": "SATURN",
      "Model": "LS"
    },
    {
      "Manufacturer": "GENERAL MOTORS CORP.",
      "NHTSACampaignNumber": "99V197000",
      "ReportReceivedDate": "/Date(932961600000-0400)/",
      "Component": "FUEL SYSTEM, GASOLINE:STORAGE:TANK ASSEMBLY",
      "Summary": "VEHICLE DESCRIPTION:  PASSENGER VEHICLES.  THESE VEHICLES DO NOT COMPLY WITH REQUIREMENTS OF FMVSS NO. 301, \"FUEL SYSTEM INTEGRITY.\"   THESE VEHICLES MAY HAVE BEEN PRODUCED WITH AN INOPERATIVE VALVE WITHIN THE FUEL TANK ASSEMBLY.",
      "Conequence": "IF A VEHICLE WITH AN INOPERATIVE VALVE WERE INVOLVED IN A ROLLOVER, FUEL SPILLAGE COULD OCCUR.",
      "Remedy": "DEALERS WILL INSPECT THE VEHICLES TO ENSURE THAT THE FUEL TANK ASSEMBLY VALVE IS OPERATING AS INTENDED.  THEY WILL REPLACE THE FUEL TANK ASSEMBLY IF NECESSARY.",
      "Notes": "OWNER NOTIFICATION BEGAN JULY 23, 1999.  OWNERS WHO TAKE THEIR VEHICLES TO AN AUTHORIZED DEALER ON AN AGREED UPON SERVICE DATE AND DO NOT RECEIVE THE FREE REMEDY WITHIN A REASONABLE TIME SHOULD CONTACT SATURN AT 1-800-553-6000, PROMPT 3.   ALSO CONTACT THE NATIONAL HIGHWAY TRAFFIC SAFETY ADMINISTRATION'S AUTO SAFETY HOTLINE AT 1-888-DASH-2-DOT (1-888-327-4236).\r\n",
      "ModelYear": "2000",
      "Make": "SATURN",
      "Model": "LS"
    },

    ...

```

## API calls with Python

```py
import requests, json
url = 'string of url'
req = request.get(url)
if(int(req.status_code) == 200):
    apiDict = json.loads(req.text)
    print(apiDict.keys())
```
