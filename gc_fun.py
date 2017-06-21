try:
    import gc_content
    have_gc = True
except ImportError as e:
    print(e)
    have_gc=false
finally:
    #Do whatever is necessary like closing files
    pass

seq = 'ACGTATATATGAGTCAGTAGTCAGTA'

if have_gc:
    print(gc_content.gc(seq))
else:
    print(seq.count('G')+seq.count('C'))
    
