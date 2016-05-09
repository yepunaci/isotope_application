import logging
import numpy as np

from rmgpy.molecule.molecule import Molecule
from rmgpy.molecule.group import Group

def compute_transfer_matrix(subgraph, graph, mapping):
    """
        
        """
    if not mapping:
        logging.error('No mappings found between subgraph:\n {}, and graph:\n {}'
                      .format(subgraph.toAdjacencyList(), graph.toAdjacencyList()))
        return

# WIP...


def main():
    result = methyl_in_ethane()
    
    print 'number of results: {}'.format(len(result))

#  for match in result:
#        print 'match: {}'.format(match)

def methyl_in_ethane_no_H():
    """
        
        """
    
    adjlist_mol_no_H = """
        1 C u0 p0 c0 {2,S}
        2 C u0 p0 c0 {1,S}
        """
    mol = Group().fromAdjacencyList(adjlist_mol_no_H)
    
    adjlist_group_no_H = """
        1 C ux p0 c0
        """
    
    group = Group().fromAdjacencyList(adjlist_group_no_H)
    
    result = mol.findSubgraphIsomorphisms(group)
    
    return result

def methyl_in_ethane():
    """
        12 possible ways to put CH3 in H3C-CH3:
        
        2 possibilities for the carbon atom
        
        3! possibilities to organize the 3 H-atoms.
        
        total = 2 * 3! = 12
        
        """
    
    adjlist_mol = """
        1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
        2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {1,S}
        5 H u0 p0 c0 {1,S}
        6 H u0 p0 c0 {2,S}
        7 H u0 p0 c0 {2,S}
        8 H u0 p0 c0 {2,S}
        """
    #mol = Group().fromAdjacencyList(adjlist_mol)
    mol=  Molecule().fromAdjacencyList(adjlist_mol)
    
    adjlist_group = """
        1 C ux p0 c0 {2,S} {3,S} {4,S}
        2 H u0 p0 c0 {1,S}
        3 H u0 p0 c0 {1,S}
        4 H u0 p0 c0 {1,S}
        """
    group = Group().fromAdjacencyList(adjlist_group)
    
    
    K= np.zeros((4,8))
    R= np.zeros((8,4))
    
    result = mol.findSubgraphIsomorphisms(group)
    
    
    for i, match in enumerate(result):
        print 'Match no: {}'.format(i)
        
        for k,v in match.iteritems():
            
            molatno = mol.atoms.index(k)
            gratno = group.atoms.index(v)
            print 'Mol atom number: {}, Group atom number: {}'.format(molatno, gratno)
            K[gratno,molatno]= K[gratno,molatno]+1
            R[molatno,gratno]= R[molatno,gratno]+1
    
    K= K / (len(result))
    R= R / (len(result))
    
    print K
    print R
    return result




######## naphthalene/benzyl radical ###########


def benzylradical_in_naphthalene():
    
    adjlist_mol = """
        1  C u0 p0 c0 {2,D} {10,S} {11,S}
        2  C u0 p0 c0 {1,D} {3,S} {12,S}
        3  C u0 p0 c0 {2,S} {4,D} {13,S}
        4  C u0 p0 c0 {3,D} {5,S} {9,S}
        5  C u0 p0 c0 {4,S} {6,D} {14,S}
        6  C u0 p0 c0 {5,D} {7,S} {15,S}
        7  C u0 p0 c0 {6,S} {8,D} {16,S}
        8  C u0 p0 c0 {7,D} {9,S} {17,S}
        9  C u0 p0 c0 {4,S} {8,S} {10,D}
        10 C u0 p0 c0 {1,S} {9,D} {18,S}
        11 H u0 p0 c0 {1,S}
        12 H u0 p0 c0 {2,S}
        13 H u0 p0 c0 {3,S}
        14 H u0 p0 c0 {5,S}
        15 H u0 p0 c0 {6,S}
        16 H u0 p0 c0 {7,S}
        17 H u0 p0 c0 {8,S}
        18 H u0 p0 c0 {10,S}
        """
    mol = Group().fromAdjacencyList(adjlist_mol)
    
    
    adjlist_group = """
        1 C u1 p0 c0 {2,S} {3,S} {4,S}
        2 H u0 p0 c0 {1,S}
        3 H u0 p0 c0 {1,S}
        4 C u0 p0 c0 {1,S} {5,T}
        5 C u0 p0 c0 {4,T} {6,S}
        6 H u0 p0 c0 {5,S}
        """
    """
        replaced with propargyl radical... doesn't work..
        """
    
    group = Group().fromAdjacencyList(adjlist_group)
    
    result = mol.findSubgraphIsomorphisms(group)
    
    return result

###############################################


if __name__ == '__main__':
    main()