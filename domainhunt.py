import pythonwhois
import string
from multiprocessing.pool import ThreadPool
import os
import psutil
import signal
import argparse
from functools import partial
import sys

# a tool for checking available 3-letter domains


class DomainHunt:

    def three_letters(self):
        char_set = string.ascii_lowercase
        string_list = []
        for h in char_set:
            for u in char_set:
                string_list.append(h + u)
        return string_list

    def whois_check(self, tlds, text):
        for i in tlds:
            url = "{} {}".format(text, i)
            print(url)
            whois = pythonwhois.get_whois(url)

            if len(whois) <= 2:
                print("domain is free")

            else:
                try:
                    print("Domain expires {:%d.%m.%Y at %H:%M:%S}".format(
                        whois["expiration_date"][0]))

                except Exception as e:
                    print("No expiration date found. Debug: " + e)

    def partil_action(self, tlds):
        try:
            whois_partial = partial(whois_check, tlds)
            p.map(whois_partial, string_list)
        except KeyboardInterrupt as e:
            p.terminate()
            p.join()
            sys.exit(0)
        except Exception as e:
            print(e)
            p.terminate()
            p.join()
        else:
            p.close()
            p.join()

    def working_init(self):
        def sig_init(signal_num, frame):
            parent = psutil.Process(parent_id)
            for child in parent.children():
                if child.pid != os.getpid():
                    print("Killing child: %s", child.pid)
                    child.kill()

            print("killing parent: %s" % parent_id)
            parent.kill()
            print("suicide: %s" % os.getpid())
            psutil.Process(os.getpid()).kill()
        # create handler (sig_int) for KeyboardInterrupt (SIGINT) signals

        signal.signal(signal.SIGINT, sig_init)


if __name__ == '__main__':
    p = DomainHunt()
    p.three_letters()
    parser = argparse.ArgumentParser(description='domainmate')
    parser.add_argument("--tlds", nargs="*", help="TLDs in use")
    parser.add_argument("--threads", type=int, help="number of threads")
    args = parser.parse_args()
    if args.threads is not None:
        p = ThreadPool(args.threads)
    else:
        p = ThreadPool(8)
    if args.tlds is not None:
        for i in args.tlds:
            if i[0] == ".":
                i = i[1:]
            p.partil_action(args.tlds)
    else:
        p.partil_action(['fi'])
