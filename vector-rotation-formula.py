df['rotated_by'] = 0

def rotate(angle, x, y):
    
    rx = np.cos(angle)*x - np.sin(angle)*y
    ry = np.sin(angle)*x + np.cos(angle)*y
    
    return rx, ry

angles = np.arange(0, 2*np.pi, 2*np.pi/100)
rotated_vectors = [rotate(angle, df['x'], df['y']) for angle in angles]
rotated_dfs = [pd.DataFrame({'x': rx, 'y': ry, 'rotated_by': [angle]*len(rx)}) for ((rx, ry), angle) in zip(rotated_vectors, angles)]

output_df = pd.concat(rotated_dfs)
output_df['rotated_by'] *= 180/np.pi


#this code is able to produce the data rotated between 0-360 degree.
