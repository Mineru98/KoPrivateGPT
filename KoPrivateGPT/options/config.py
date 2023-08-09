import os
import pathlib


class Options(object):
    root_dir = pathlib.PurePath(os.path.dirname(os.path.realpath(__file__))).parent.parent
    source_dir = os.path.join(root_dir, "SOURCE_DOCUMENTS")
    embedded_files_cache_dir = os.path.join(root_dir, "embedded_files_cache.pkl")
    bm25_db_dir = os.path.join(root_dir, "bm25_db.pkl")
    HwpConvertOpt = 'all'  # 'main-only'
    HwpConvertHost = f'http://hwp-converter:7000/upload?option={HwpConvertOpt}'


class ChromaOptions(object):
    persist_dir = os.path.join(Options.root_dir, "DB")
    if not os.path.exists(persist_dir):
        os.makedirs(persist_dir)
    collection_name = "test"  # you can modify this to change your own collection name


class PineconeOptions(object):
    namespace = "pinecone-namespace"
