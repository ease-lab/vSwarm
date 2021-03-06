#!/usr/bin/env python3

# MIT License
#
# Copyright (c) 2021 Francisco Romero, Clemente Farias Canepa,
# Sadjad Fouladi, StanfordSNR, and EASE lab.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os

GG_DIR = os.environ.get('GG_DIR')

if not GG_DIR:
    raise Exception("GG_DIR environment variable not set")

if not os.path.isabs(GG_DIR):
    raise Exception("GG_DIR must be an absolute path")

class GGPaths:
    blobs = os.path.join(GG_DIR, "blobs")
    reductions = os.path.join(GG_DIR, "reductions")

    @classmethod
    def blob_path(cls, blob_hash):
        return os.path.join(cls.blobs, blob_hash)

    @classmethod
    def reduction_path(cls, blob_hash):
        return os.path.join(cls.reductions, blob_hash)

    @classmethod
    def object_url(cls, bucket, key):
        return "https://{bucket}.s3.amazonaws.com/{key}".format(bucket=bucket, key=key)

class GGCache:
    @classmethod
    def check(cls, thunk_hash, output_tag=None):
        key = thunk_hash
        if output_tag:
            key += ("#%s" % output_tag)

        rpath = GGPaths.reduction_path(key)

        if not os.path.exists(rpath):
            return None

        with open(rpath, "r") as fin:
            data = fin.read()
            data = data.split(" ")
            return data[0]

    @classmethod
    def insert(cls, old_hash, new_hash):
        rpath = GGPaths.reduction_path(old_hash)

        with open(rpath, "w") as fout:
            fout.write(new_hash)

def make_gg_dirs():
    os.makedirs(GGPaths.blobs, exist_ok=True)
    os.makedirs(GGPaths.reductions, exist_ok=True)

make_gg_dirs()
