from multiprocessing import Pool
from flask import Flask

app = Flask(__name__)
_pool = None

def double_f(x):
    return x*x

@app.route('/double_calc/<int:x>')
def expcalc(x):
    
    f = _pool.map(expensive_function, range(5))
    #f = _pool.apply_async(double_f,[x])
    #r = f.get(timeout=2)
    return 'Result is'+str(f)

if __name__=='__main__':
    _pool = Pool(processes=4)
    try:
        app.run()
    except KeyboardInterrupt:
        _pool.close()
        _pool.join()