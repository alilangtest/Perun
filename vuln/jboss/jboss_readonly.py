#!/usr/bin/env python
# -*- coding:utf-8 -*-

class VulnChecker(VulnCheck):
    def __init__(self, ip_and_port_list):
        self._name = 'jboss_readonly'
        self.info = "Check if the JBoss path /invoker/readonly exists for CVE-2017-12149"
        self.keyword = ['all', 'jboss', 'rce', 'cve_2017_12149', 'web', 'intranet', 'danger', '8080']
        self.default_ports_list = WEB_PORTS_LIST
        VulnCheck.__init__(self, ip_and_port_list)

    def _check(self, ip, port):
        result = "Maybe jBoss vuln CVE-2017-12149"
        url1 = "http://%s:%d/invoker/readonly"%(ip, int(port)) if add_web_path == "" else "http://%s:%d/%s/invoker/readonly"%(ip, int(port), add_web_path)
        url2 = "https://%s:%d/invoker/readonly"%(ip, int(port)) if add_web_path == "" else "https://%s:%d/%s/invoker/readonly"%(ip, int(port), add_web_path)
        try:
            req = Requester(url1, method='HEAD')
            if (req.code == 500 or (req.code == 200 and check_200_or_404(url1))) and ('JBoss'.lower() in req.headers.lower() or 'Apache-Coyote/1.1'.lower() in req.headers.lower()):
                self._output(ip, port, result)
        except RequesterOpenError:
            try:
                req = Requester(url2, method='HEAD')
                if (req.code == 500 or (req.code == 200 and check_200_or_404(url2))) and ('JBoss'.lower() in req.headers.lower() or 'Apache-Coyote/1.1'.lower() in req.headers.lower()):
                    self._output(ip, port, result)
            except:
                pass
        except:
            pass

globals()['VulnChecker'] = VulnChecker