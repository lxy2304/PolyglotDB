__all__ = ['query', 'io', 'corpus', 'config', 'exceptions', 'CorpusContext', 'CorpusConfig']


__ver_major__ = 1
__ver_minor__ = 3
__ver_patch__ = 0
__version__ = f"{__ver_major__}.{__ver_minor__}.{__ver_patch__}"



import polyglotdb.query.annotations as graph

import polyglotdb.io as io

import polyglotdb.corpus as corpus

import polyglotdb.exceptions as exceptions

import polyglotdb.config as config

CorpusConfig = config.CorpusConfig

CorpusContext = corpus.CorpusContext
