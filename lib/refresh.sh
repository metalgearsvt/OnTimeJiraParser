#!/bin/bash
curl 'https://DOMAIN.COM/web/api/v4/tasks?filter_id=645&include_archived=false' -s -H 'Pragma: no-cache' -H 'Accept-Encoding: gzip, deflate, sdch' -H 'Accept-Language: en-US,en;q=0.8' -H 'X-Authorization: OAuth XXXXX' -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36' -H 'Accept: */*' -H 'Cache-Control: no-cache' -H 'X-Requested-With: XMLHttpRequest' -H 'Cookie: ASP.NET_SessionId=XXXXX; client_oauth_token=XXXXX; .ASPXAUTH=XXXXX' -H 'Connection: keep-alive' -H 'Referer: https://DOMAIN.COM/web/default.aspx' --compressed > ./lib/onTimeOutput.out
