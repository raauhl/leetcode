
def k_smallest_pairs(nums1, nums2, k):
    i = j = 0
    m, n = len(nums1), len(nums2)
    pairs = [(nums1[0], nums2[0])]
    x = 1

    while x < k:
        if i == m-1 and j == n-1:
            pairs.append((nums1[i], nums2[j]))
        elif i == m-1:
            j += 1
            pairs.append((nums1[i], nums2[j]))
        elif j == n-1:
            i += 1
            pairs.append((nums1[i], nums2[j]))
        else:
            if nums1[i+1]+nums2[j] < nums1[i]+nums2[j+1]:
                i += 1
            else:
                j += 1
            pairs.append((nums1[i], nums2[j]))
        x += 1

    return pairs

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3

pairs = k_smallest_pairs(nums1, nums2, k)
print(pairs)

        

        



